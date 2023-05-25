def align(img, g_coord):
    import numpy
    from skimage import img_as_float

    def coor(img, g):
        d = 15
        correlation_r = {}
        for row_shift in range(-d, d + 1):
            ry = numpy.roll(img, row_shift, axis=1)
            for col_shift in range(-d, d + 1):
                rx = numpy.roll(ry, col_shift, axis=0)
                correlation_r[(row_shift, col_shift)] = (rx * g).sum()
        return max(correlation_r, key=correlation_r.get)

    img = img_as_float(img)
    yg, xg = g_coord
    per = 10
    v, s = img.shape
    v //= 3
    frv = int(v / 100 * per)
    frs = int(s / 100 * per)
    b = img[frv:v - frv, frs:s - frs]
    g = img[v + frv:v * 2 - frv, frs:s - frs]
    r = img[v * 2 + (img.shape[0] - v * 3) + frv:img.shape[0] - frv, frs:s - frs]
    r_coord = coor(r, g)
    b_coord = coor(b, g)
    yb = yg - v - b_coord[1]
    xb = xg - b_coord[0]
    yr = yg + v - r_coord[1]
    xr = xg - r_coord[0]
    return (yb, xb), (yr, xr) 