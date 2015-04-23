from itertools import permutations
from random import choice
from collections import Counter

NEG_INF = float("-inf")

memo = {}

def relation_pass(treat, relation, to):
    if not relation:
        return True
    if relation == "higher":
        return treat > to
    if relation == "lower":
        return treat < to
    if relation == "equal":
        return treat == to

def happiness(treats, relation = None, to = None):

    if len(treats) == 1:
        if not relation_pass(treats[0], relation, to):
            return NEG_INF, tuple()
        if relation == "higher":
            return 1, treats
        if relation == "lower":
            return -1, treats
        if relation == "equal":
            return 0, treats

    try: 
        return memo[(treats, relation, to)]
    except KeyError:
        pass

    top, order = NEG_INF, tuple()
    
    tried_treats = set()

    for t, treat in enumerate(treats):
        if treat in tried_treats:
            continue
        if not relation_pass(treat, relation, to):
            continue
        
        if relation == None:
            print(t)
        tried_treats.add(treat)

        new_treats = treats[:t] + treats[t+1:]
        
        top1, order1 = happiness(new_treats, "higher", treat)
        top2, order2 = happiness(new_treats, "equal", treat)
        top3, order3 = happiness(new_treats, "lower", treat)
        
        order1 = (treat,) + order1
        order2 = (treat,) + order2
        order3 = (treat,) + order3

        if not relation or relation == "lower":
            top1 -= 1
        if not relation or relation == "higher":
            top3 += 1


        top, order = max(
            (top, order),
            (top1, order1), 
            (top2, order2), 
            (top3, order3))

    memo[(treats, relation, to)] = (top, order)

    return top, order

def puppy_score(n, treats):
    if n == 0:
        if treats[0] == treats[1]:
            return 0
        return -1 if treats[0] < treats[1] else 1
    if n == len(treats) - 1:
        if treats[-1] == treats[-2]:
            return 0
        return -1 if treats[-1] < treats[-2] else 1

    p1, p2, p3 = treats[n-1], treats[n], treats[n+1]

    if p1 > p2 and p3 > p2:
        return -1
    if p1 < p2 and p3 < p2:
        return 1

    return 0

def simple_happiness(treats):
    puppy_count = len(treats)

    top, order = NEG_INF, tuple()
    
    for perm in permutations(treats):
        score = sum(puppy_score(n, perm) for n in range(puppy_count))
        
        top, order = max((top,order), (score, perm))

    return top, order

if __name__ == "__main__":
    target = 1
    happy = 0
    treats = None
    order = None

    while happy < target:
        puppies = 30
        space = list(range(1, 13))

        treats = tuple(sorted(choice(space) for _ in range(puppies)))
        print(treats)
        happy, order = happiness(treats)

        print(happy, order)


