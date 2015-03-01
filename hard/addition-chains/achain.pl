:- use_module(library(clpfd)).

find_chain(Length, Target, Chain) :-
    L is Length - 3,
    length(Vars, L),
    append([[1,2], Vars, [Target]], Chain),
    [1,2|Rest] = Chain,
    star_chain([2,1], Rest, Target, 2, Length).

find_chain(Length, Target, Chain) :-
    write("No star chain found, checking other chains...\n"),
    L is Length - 3,
    length(Vars, L),
    append([[1,2], Vars, [Target]], Chain),
    [1,2|Rest] = Chain,
    bind_vars([2,1], Rest, Target, 2, Length).

star_chain(Prev, [Target], Target, _, _) :-
    [P|_] = Prev,
    member(A, Prev),
    Target =:= A + P.

star_chain(Prev, [Curr|Rest], Target, Index, Length) :-
    Rest \= [],
    [P|_] = Prev,
    star_step(Prev, Curr),
    Curr > P,
    Curr =< Target,
    Target =< Curr ** (Length - Index + 1),

    Index2 is Index + 1,

    star_chain([Curr|Prev], Rest, Target, Index2, Length).

bind_vars(Prev, [Target], Target, _, _) :-
    [P|_] = Prev,
    member(A, Prev),
    Target =:= A + P.

bind_vars(Prev, [Curr|Rest], Target, Index, Length) :- 
    Rest \= [],
    [P1, P2|_] = Prev,
    (P1 =:= P2 << 1 ->
        star_step(Prev, Curr);
        regular_step(Prev, Curr) 
    ),
    Curr > P1,    
    Curr =< Target,
    Target =< Curr ** (Length - Index + 1),
    
    Index2 is Index + 1,

    bind_vars([Curr|Prev], Rest, Target, Index2, Length).

regular_step(Prev, Curr) :- star_step(Prev, Curr).
regular_step(Prev, Curr) :- non_star_step(Prev, Curr).

star_step([P|Prev], Curr) :-
    member(A, [P|Prev]),
    Curr is P + A.

non_star_step([_|Prev], Curr) :-
    member(A, Prev), member(B, Prev),
    Curr is A + B.
