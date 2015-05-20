import sys

from random import random

def get_points(n):
    return [(random(), random()) for _ in range(n)]

if __name__ == "__main__":
    count = int(sys.argv[1])

    points = get_points(count)
    print(count)
    for (x,y) in points:
        print("{:.8f} {:.8f}".format(x, y))
