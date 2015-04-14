:- use_module(library(clpfd)).


find_chain(Length, Target, Chain) :-
    L is Length - 2,
    length(Vars, L),
    append([[1,2], Vars, [Target]], Chain),
    [1,2|Rest] = Chain,
    bind_vars([2,1], Rest, Target, 2, Length).


bind_vars(Prev, [Target], Target, _, _) :-
    !,
    [P|_] = Prev,
    member(A, Prev),
    Target =:= A + P.

bind_vars(Prev, [Curr|Rest], Target, Index, Length) :- 
    Rest \= [],
    [P1|_] = Prev,
    member(A, Prev),
    member(B, Prev),
    B =< A,
    Curr is A + B,
    %ub(Curr, Ub),
    %Index =< Ub,
    Curr > P1,    
    %Curr =< Target,
    
    Target =< Curr ** (Length - Index + 1),
    
    Index2 is Index + 1,

    bind_vars([Curr|Prev], Rest, Target, Index2, Length).

ub(N, M) :- 
    lambda(N, M1),
    nu(N, M2),
    M is M1 + M2 - 1.

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
