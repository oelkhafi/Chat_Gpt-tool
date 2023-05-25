# Output format

# If the system has no solution, then the program should print a single number 0. (OK_2)

# If the system has infinitely many solutions, each of which looks like y=kx+b,
# then the program should print the number 1, and then the values k and b. (OK_6)

# If the system has a single solution (x0, y0),
# then the program should print the number 2, and then the values x0 and y0. (OK_3)

# If the system has infinitely many solutions that look like x=x0 with any y,
# then the program should output the number 3, and then the value x0. (OK_5)

# If the system has infinitely many solutions that look like y=y0 with any x,
# then the program should output the number 4, and then the value y0. (OK_4)

# If any pair of numbers (x,y) is a solution, the program should output the number 5. (OK_1)

a, b, c, d, e, f = (float(input()) for _ in range(6))
Det = a * d - b * c
d_x, d_y = e * d - b * f, a * f - c * e

if a == b == c == d == e == f == 0:
    print(5)

elif a == b == 0 and e != 0 or c == d == 0 and f != 0:
    print(0)

elif Det != 0:
    print(2, d_x / Det, d_y / Det)

else:
    if a < 0:
        a, b, e = -a, -b, -e

    if c < 0:
        c, d, f = -c, -d, -f

    if a < c:
        a, b, e, c, d, f = c, d, f, a, b, e

    if a != 0:
        a, b, e = 1, b / a, e / a
        c, d, f = 0, d - c * b, f - c * e

        if d != 0:
            d, f = 1, f / d
            b, e = 0, e - c * f

        if a == b == 0 and e != 0 or c == d == 0 and f != 0:
            print(0)

        elif b != 0:
            a, b, e = a / b, 1, e / b
            print(1, -a, e)
        else: # a != 0, b == 0
            print(3, e / a)

    else: # a == 0
        if b == 0 and e != 0 or d == 0 and f != 0:
            print(0)

        elif b != 0 and d == 0:
            print(4, e / b)

        elif b == 0 and d != 0:
            print(4, f / d)

        elif b != 0 and d != 0 and e / b != f / d:
            print(0)

        elif b != 0 and d != 0 and e / b == f / d:
            print(4, e / b)
 