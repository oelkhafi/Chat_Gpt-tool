import skimage.io as sio
from itertools import repeat

def getWalker(startP, endP):
    """""" Return point iterator. Each call of it will return
        a point. Iterator begin from startP, and
        finish at the endP inclusive. """"""
    if startP == endP:
        return [startP]
    def getIter(start, end):
        if start == end:
            return repeat(start)
        if start < end:
            return range(start, end+1)
        return range(start, end-1, -1)
    coordIterators = [getIter(startP[coord], endP[coord])
                      for coord in range(len(startP))]
    return zip(*coordIterators)

def countStepsUntil(walker, pred):
    cnt = 0
    for point in walker:
        if not pred(point):
            return cnt
        cnt += 1
    return 0

def frameShape(img):
    frameCol = img[0, 0]
    height, width, _ = img.shape
    cRow = height // 2
    cCol = width // 2
    zone = 50
    # Each direction is a tuple of:
    #   - start point (col, row);
    #   - endpoint (col, row).
    directions = [ # from the center of the left border by columns
                  ((cRow, 0), (cRow, zone)),
                    # from the center of the top border by rows
                  ((0, cCol), (zone, cCol)),
                    # from the center of the right border by columns
                  ((cRow, width-1), (cRow, width-1-zone)),
                    # from the center of the bottom border by rows
                  ((height-1, cCol), (height-1-zone, cCol))]
    return tuple(map(lambda d:
                     countStepsUntil(getWalker(*d),
                                     lambda p: all(img[p] == frameCol)),
                     directions))

img = sio.imread('img.png')
print(*frameShape(img), sep=' ') 