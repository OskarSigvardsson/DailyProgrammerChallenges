
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, M) :- recorded(N, M), !.
fibonacci(N, M) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, M1),
    fibonacci(N2, M2),
    M is M1 + M2,
    recorda(N, M).


factorial(N, M) :- factorial(N, 1, M).

factorial(0, X, X) :- !.
factorial(N, Acc, M) :-
    N > 0, 
    N1 is N - 1,
    Acc1 is Acc * N,
    factorial(N1, Acc1, M).
