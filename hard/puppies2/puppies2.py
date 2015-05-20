import sys

from math import sqrt
from random import random, shuffle
from time import time
from bintrees import FastRBTree as RBTree

POS_INF = float('inf')
NEG_INF = float('-inf')

def get_points(n):
    return [(random(), random()) for _ in range(n)]

def read_input():
    count = sys.stdin.readline()
    return [tuple(map(float, l.split())) for l in  sys.stdin.readlines()]


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def naive_tour(start, points):
    x, y = start
    tour = []
    total_dist = 0.0
    
    while len(points) > 0:
        d, p = min((dist((x,y), p), p) for p in points)
        points.remove(p)
        x, y = p
        total_dist += d
        tour += [p]

    return total_dist, tour

def better_tour(start, points):
    xaxis = RBTree((x, (x,y)) for (x,y) in points)
    
    p = start

    xaxis.insert(NEG_INF, (NEG_INF, 0.5))
    xaxis.insert(POS_INF, (POS_INF, 0.5))

    tour = []
    tour_length = 0

    while len(xaxis) > 2:
        x, y = p
        lx, left = xaxis.floor_item(x)
        rx, right = xaxis.ceiling_item(x)
        md, mp = min((dist(p, left), left), (dist(p, right), right))

        while x - lx <= md or rx - x <= md:
            try:
                lx, left  = xaxis.prev_item(lx)
            except KeyError:
                lx, left = NEG_INF, (NEG_INF, 0.5)

            try:
                rx, right = xaxis.succ_item(rx)
            except KeyError:
                rx, right = POS_INF, (POS_INF, 0.5)


            md, mp = min(
                (dist(p, left), left), 
                (dist(p, right), right),
                (md, mp))

        p = mp
        tour.append(mp)
        tour_length += md
        xaxis.remove(mp[0])

    return tour_length, tour


def better_tour_2(start, points):
    xaxis = RBTree((x, (x,y)) for (x,y) in points)
    yaxis = RBTree((y, (x,y)) for (x,y) in points)
    p = start

    xaxis.insert(NEG_INF, (NEG_INF, 0.5))
    xaxis.insert(POS_INF, (POS_INF, 0.5))
    yaxis.insert(NEG_INF, (0.5, NEG_INF))
    yaxis.insert(POS_INF, (0.5, POS_INF))

    tour = []
    tour_length = 0

    while len(xaxis) > 2:
        x, y = p
        lx, left = xaxis.floor_item(x)
        rx, right = xaxis.ceiling_item(x)
        ty, top = yaxis.floor_item(y)
        by, bottom = yaxis.ceiling_item(y)

        md, mp = min(
            (dist(p, left), left), 
            (dist(p, right), right),
            (dist(p, top), top),
            (dist(p, bottom), bottom)
        )

        dx1 = x - lx
        dx2 = rx - x
        dy1 = y - by 
        dy2 = ty - y

        while dx1 <= md or dx2 <= md or dy1 <= md or dy2 <= md:
            dx1 = x - lx
            dx2 = rx - x
            dy1 = y - by 
            dy2 = ty - y
            if dx1 <= md:
                try:
                    lx, left  = xaxis.prev_item(lx)
                    dl = dist(p, left)
                except KeyError:
                    lx, left = NEG_INF, (NEG_INF, 0.5)
            
            if dx2 <= md:
                try:
                    rx, right = xaxis.succ_item(rx)
                except KeyError:
                    rx, right = POS_INF, (POS_INF, 0.5)

            if dy1 <= md:
                try:
                    by, bottom  = yaxis.prev_item(by)
                except KeyError:
                    by, bottom = NEG_INF, (0.5, NEG_INF)
            
            if dy2 <= md:
                try:
                    ty, top = xaxis.succ_item(ty)
                except KeyError:
                    ty, top = POS_INF, (POS_INF, 0.5)

            md, mp = min(
                (dist(p, left), left), 
                (dist(p, right), right),
                (dist(p, top), top), 
                (dist(p, bottom), bottom),
                (md, mp))

        p = mp
        tour.append(mp)
        tour_length += md
        xaxis.remove(mp[0])
        yaxis.remove(mp[1])

    return tour_length, tour

if __name__ == "__main__":
    points = read_input()
    #print(points)
    #exit()
    #points = get_points(100000)

    #points = [
    #(0.9, 0.7),
    #(0.7, 0.7),
    #(0.1, 0.1),
    #(0.4, 0.1),
    #(0.6, 0.6),
    #(0.8, 0.8)
    #]
    
    shuffle(points)

    #t1 = time()
    #td1, tr1 = naive_tour((0.5,0.5), points[:])
    #t1 = time() - t1

    t2 = time()
    td2, tr2 = better_tour((0.5, 0.5), points[:])
    t2 = time() - t2

    #print(t1, td1)
    print(t2, td2)
    #print(tr2)
    #print(tr1 == tr2)

