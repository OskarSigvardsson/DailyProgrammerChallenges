:- use_module(bfs).

test :- 
    shortest_path(m, a, e, L),
    write(L), nl.

m(X, Y) :- n(X, Y).
m(X, Y) :- n(Y, X).

n(a, b).
n(b, x).
n(x, y).
n(y, z).
n(z, q).
n(c, d).
n(d, e).
n(a, f).
n(f, g).
n(g, e).

