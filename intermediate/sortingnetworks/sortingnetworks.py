import sys

def chain(it):
    from itertools import chain

    return list(chain.from_iterable(it))

def weave(order, offset):
    if(order == 0):
        return []
    return [(offset + n, offset + n + 2**(order-1)) for n in range(2**(order-1))]

def optimal_4_wires():
    return [(0,2), (1,3), (0,1), (2,3), (1,2)]

def batcher_8_wires():
    return chain([
        optimal_4_wires(),
        [(a+4,b+4) for a,b in optimal_4_wires()],
        [(0,4),(1,5),(2,6),(3,7)],
        [(2,4),(3,5)],
        [(1,2),(3,4),(5,6)]])

def bad_batcher_8_wires():
    return batcher_8_wires()[:-1] + [(6,7)]

def optimal_16_wires():
    comparators = chain([
        chain(weave(1, offset) for offset in range(0, 16, 2)), 
        chain(weave(2, offset) for offset in range(0, 16, 4)), 
        chain(weave(3, offset) for offset in range(0, 16, 8)), 
        chain(weave(4, offset) for offset in range(0, 16, 16))]) 

    comparators += [
        ( 5, 10), ( 6,  9), ( 3, 12), ( 7, 11), (13, 14), ( 1, 2), ( 4,  8),
        ( 1,  4), ( 7, 13), ( 2,  8), (11, 14), ( 2,  4), ( 5, 6), ( 9, 10),
        (11, 13), ( 3,  8), ( 7, 12), ( 6,  8), ( 3,  5), ( 7, 9), (10, 12),
        ( 3,  4), ( 5,  6), ( 7,  8), ( 9, 10), (11, 12), ( 6, 7), ( 8, 9)]

    return comparators

def bad_16_wires():
    return optimal_16_wires()[:-1] + [(12,13)]
def run_network(network, inputs):
    ns = inputs[:]
    for (a,b) in network:
        if ns[a] > ns[b]:
            ns[a], ns[b] = ns[b], ns[a]

    return ns

def check_network(network):
    wires = max(chain(network)) + 1
    fail_count = 0

    for n in range(2**wires):
        inputs = [int(d) for d in ("{:0>"+str(wires)+"b}").format(n)]
        if sorted(inputs) != run_network(network, inputs):
            print(("Failed on {:0>"+str(wires)+"b}").format(n))
            fail_count += 1

    return fail_count

def replace(l, a, b):
    for i, x in enumerate(l):
        if x == a:
            l[i] = b

def odd_even_merge(order, offset=0):
    if order == 0:
        return []
    
    comparators = chain([odd_even_merge(order-1, offset),
                         odd_even_merge(order-1, offset + 2**(order-1)),
                         weave(order, offset)])

    for n in range(order):
        for w in range(1,2**n+1):
            comparators += weave(order - n - w, offset + (w+1) * 2**(order-n-2))

    return comparators

def print_network(network):
    wires = max(chain(network)) + 1
    comps = len(network)

    print("{} {}".format(wires, comps))

    for (a,b) in network:
        print("{} {}".format(a, b))

def read_network():
    sys.stdin.readline()
    network = []

    for line in sys.stdin:
        network.append(tuple(map(int, line.split(" "))))

    return network

if __name__ == "__main__":
    network = read_network()
    print_network(network)
    print(check_network(network))
