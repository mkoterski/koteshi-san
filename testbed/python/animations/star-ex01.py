#!/usr/bin/python

import sys, math, time, random

def distance(x, y):
    # ((y - y_center) * 2) -> correct ratio for a true circle
    return math.ceil(math.sqrt(((x - 40) ** 2) + (((y - 12) * 2) ** 2)))

def star(radiuses):
    for r in radiuses:
        #~ clear screen: http://stackoverflow.com/a/2084521/2257664
        print(chr(27) + "[2J")

        # width
        for y in range(24):
            # height
            for x in range(80):
                d = distance(x, y)

                #~ border
                if (d == r):
                    sys.stdout.write('*')
                #~ inside the star
                elif (d < r):
                    if (r > 35):
                        sys.stdout.write(' ')
                    elif (r > 25) and ((d % 2) != 0):
                        sys.stdout.write('-')
                    elif (r > 15) and ((d % 2) == 0):
                        sys.stdout.write(' ')
                    else :
                        sys.stdout.write(random.choice('****#@'))
                #~ space outside the star
                else:
                    sys.stdout.write(' ')
            print()
        time.sleep(0.1)

star(list(range(0, 12)) + list(range(10, 0, -1)) + list(range(0, 50)))