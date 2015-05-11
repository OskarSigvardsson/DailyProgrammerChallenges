NEG_INF = float("-inf")

# I should probably use one of those fancy enums for this
ANY = 0
HIGHER = 1
EQUAL = 2
LOWER = 3

# Memoization dictionary
memo = {}

# Is <treat> higher/lower/equal to <to>
def relation_pass(treat, relation, to):
    if relation == ANY:
        return True
    if relation == HIGHER:
        return treat > to
    if relation == LOWER:
        return treat < to
    if relation == EQUAL:
        return treat == to

# Lets calculate optimal happiness!
def happiness(treats, relation = ANY, to = None):

    # Recursion base case
    if len(treats) == 1:
        if not relation_pass(treats[0], relation, to):
            return NEG_INF, tuple()
        if relation == HIGHER:
            return 1, treats
        if relation == LOWER:
            return -1, treats
        if relation == EQUAL:
            return 0, treats

    # Check if we've already seen this subproblem. If we have, return that,
    # otherwise proceed
    try: 
        return memo[(treats, relation, to)]
    except KeyError:
        pass

    top, order = NEG_INF, tuple()
    
    tried_treats = set()

    # Loop over the treats
    for t, treat in enumerate(treats):

        # Is the current treat valid for our relation?
        if not relation_pass(treat, relation, to):
            continue

        # If we've already tried this treat, skip this round. Doesn't change
        # the asymptotic running time, but saves a few function calls and
        # hash-lookups. 
        if treat in tried_treats:
            continue
        
        tried_treats.add(treat)

        # New treat list for recursion. If the input treats are sorted, this
        # will be as well, which is crucial for the memoization dictionary
        new_treats = treats[:t] + treats[t+1:]
        
        # Recurse!
        top1, order1 = happiness(new_treats, HIGHER, treat)
        top2, order2 = happiness(new_treats, EQUAL, treat)
        top3, order3 = happiness(new_treats, LOWER, treat)
        
        order1 = (treat,) + order1
        order2 = (treat,) + order2
        order3 = (treat,) + order3

        # Modify score based on what the relation is for this call and the
        # recursion
        if relation == ANY or relation == LOWER:
            top1 -= 1
        if relation == ANY or relation == HIGHER:
            top3 += 1

        # Which is our winner?
        top, order = max(
            (top, order),
            (top1, order1), 
            (top2, order2), 
            (top3, order3))

    # Save calculated subproblem
    memo[(treats, relation, to)] = (top, order)

    return top, order

if __name__ == "__main__":
    # The algorithm relies on the inputs being a tuple of sorted integers, so
    # lets just make sure
    treats = tuple(sorted(map(int, 
        "1 1 2 2 2 2 2 2 3 4 4 4 5 5 5 6 6 6 7 7 8 8 9 9 9 9 9 9 9 9".split())))

    # Calculate!
    happiness, order = happiness(treats)
    
    # Print!
    print happiness
    print " ".join(str(x) for x in order)
