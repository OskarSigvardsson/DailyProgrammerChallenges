from __future__ import division

import sys

from itertools import *
from random import random
from decimal import Decimal

def naive_subset_sum(vals, target):
    best_sum = 0
    best_comb = ()
    for comb in chain.from_iterable(combinations(vals, r) for r in range(len(vals)+1)):
        s = sum(comb)
        if s <= target and s > best_sum:
            best_sum = s
            best_comb = comb

    return best_sum, best_comb

def subset_sum(vals, target):
    print("Calculating first half...")
    l1 = all_subsets_sorted(vals[:len(vals)//2], target)
    print("Calculating second half...")
    l2 = all_subsets_sorted(vals[len(vals)//2:], target)
    print("Combining...")

    best_sum = 0
    best_comb = 0

    i = len(l1) - 1
    j = 0

    while i >= 0 and j < len(l2):
        s1, c1 = l1[i]
        s2, c2 = l2[j]
        
        s = s1 + s2

        if s <= target and s > best_sum:
            best_sum = s
            best_comb = c1 + c2

        if s < target:
            j+=1
        elif s > target:
            i-=1
        else:
            return (s, c1 + c2)

    return best_sum, best_comb


class Link:
    def __init__(self, val, next_link=None):
        self.val = val
        self.next_link = next_link

def all_subsets_sorted(vals, target):
    combs = [(0, ())]

    for vi, val in enumerate(vals):

        combs1 = combs
        combs2 = [0] * len(combs)
       
        for (i, (s, c)) in enumerate(combs):
            if s + val == target:
                print("Hit!")
            combs2[i] = ((s + val, c + (val,)))

        combs3 = [0] * (2*len(combs1))
        i, j, k = 0,0,0
        

        while i < len(combs1) or j < len(combs2):
            if k % 1000 == 0:
                sys.stdout.write("{} / {}: {:%}\r".format(vi, len(vals), k / len(combs3)))
                sys.stdout.flush()
            if i >= len(combs1):
                combs3[k] = (combs2[j])
                j+=1
            elif j >= len(combs2):
                combs3[k] = (combs1[i])
                i+=1
            else:
                s1, c1 = combs1[i]
                s2, c2 = combs2[j]

                if s1 < s2:
                    combs3[k] = (combs1[i])
                    i+=1
                else:
                    combs3[k] = (combs2[j])
                    j+=1
            
            k+=1
        combs = combs3
    
        sys.stdout.write("{} / {}\r".format(vi, len(vals)))
        sys.stdout.flush()

    print("")

    return combs

if __name__ == "__main__":
    

    #r1 = naive_subset_sum(vals, target)

    ns = 46
    target = Decimal(13)

    vals = [Decimal(str(random())[:9]) for _ in range(ns)]
    #target = Decimal(ns)//2
    
    print(target)
    print(ns)
    for val in vals:
        print(val)

    vals = [int(v * 10**7) for v in vals]
    target = int(target * 10**7)


    r2 = subset_sum(vals, target)
    
    print("----")
    hit = Decimal(r2[0]) / 10**7
    vs = [Decimal(r) / 10**7 for r in r2[1]]
    print(hit)
    for r in vs:
        print(r)
        
    #print(str(hit) + " = " + " + ".join(str(r) for r in vs))

    #cs = all_subsets_sorted([1,2,3,4], 100)
    #
    #for c in cs:
    #    print(c)

