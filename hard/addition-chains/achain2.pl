binary_exponents(N, Bs) :- 
    binary_exponents(N, 0, Bs).

binary_exponents(0, _, []) :- !.
binary_exponents(N, Pos, Rest) :-
    N > 0,
    0 =:= N /\ 1, !,
    Pos1 is Pos + 1,
    N1 is N >> 1,
    binary_exponents(N1, Pos1, Rest).
     
binary_exponents(N, Pos, [Pos|Rest]) :-
    N > 0,
    1 =:= N /\ 1, !,
    Pos1 is Pos + 1,
    N1 is N >> 1,
    binary_exponents(N1, Pos1, Rest).

pairs(N, Ps) :-
    divisors(N, Ds),
    findall(P, pair(N, Ds, P), Ps).

pair(N, Ds, A-B) :- 
    member(A, Ds),
    member(B, Ds),
    A =< B,
    A*B =:= N.

divisors(N, Ds) :-
    findall(D, divisor(N, D), Ds1),
    sort(Ds1, Ds).
    
divisor(N, D) :-
    factors(N, Fs),
    length(Fs, L),
    length(Facs, L),
    bind_facs(Facs, Fs),
    prod(Facs, D).

mul(A, B, C) :- C is A*B.
prod(Fs, P) :- foldl(mul, Fs, 1, P).

bind_facs([], []).
bind_facs([Fact|Rest], [N-M|Ns]) :-
    between(0, M, E),
    Fact is N**E,
    bind_facs(Rest, Ns).

factors(N, [2-M|Fs]) :- 
    0 =:= N /\ 1, !,
    multiplicity(N, 2, 0, M, N1),
    factors(N1, 3, Fs).

factors(N, Fs) :-
    1 =:= N /\ 1, !,
    factors(N, 3, Fs).

factors(1, _, []) :- !.
factors(N, D, [N-1]) :- D*D > N, !.
factors(N, D, [D-M|Fs]) :-
    D*D =< N, 
    multiplicity(N, D, 0, M, N1), 
    M > 0, !,
    D1 is D + 2,
    factors(N1, D1, Fs).

factors(N, D, Fs) :- 
    D*D =< N,
    multiplicity(N, D, 0, 0, N), !,
    D1 is D + 2,
    factors(N, D1, Fs).

multiplicity(N, D, X, X, N) :- N mod D =\= 0, !.
multiplicity(N, D, Acc, Result, NumberLeft) :-
    N mod D =:= 0, !,
    N1 is N / D,
    Acc1 is Acc + 1,
    multiplicity(N1, D, Acc1, Result, NumberLeft).


lambda(N, M) :- lambda(N, 0, M).

lambda(1, X, X) :- !.
lambda(N, Acc, M) :-
    N > 1, !,
    N1 is N >> 1,
    Acc1 is Acc + 1,
    lambda(N1, Acc1, M).

nu(N, M) :- nu(N, 1, M).
nu(1, X, X) :- !.
nu(N, Acc, M) :- 
    N > 1, !,
    N1 is N >> 1,
    (
    N /\ 1 =:= 0 ->
        Acc1 is Acc;
        Acc1 is Acc + 1
    ),
    nu(N1, Acc1, M).
