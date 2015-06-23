:- module(bfs, [shortest_path/4]).
:- use_module(library(rbtrees)).

shortest_path(Np, Start, Finish, Length) :-
    rb_empty(Visited),
    rb_empty(Frontier1),
    rb_empty(Next),
    rb_insert(Frontier1, Start, 0, Frontier2),
    shortest_path(Np, Finish, Frontier2, Next, Visited, Length).

shortest_path(_, Finish, _, _, Visited, Length) :-
    rb_lookup(Finish, Length, Visited), !.

shortest_path(_, _, Frontier, Next, _, _) :-
    rb_empty(Frontier),
    rb_empty(Next),
    !,
    fail.

shortest_path(Np, Finish, FrontierIn, Next, Visited, Length) :-
    rb_empty(FrontierIn), 
    rb_empty(FrontierOut), !,
    shortest_path(Np, Finish, Next, FrontierOut, Visited, Length).

shortest_path(Np, Finish, FrontierIn, NextIn, VisitedIn, Length) :-
    rb_del_min(FrontierIn, Node, D1, FrontierOut),
    (rb_lookup(Node, _, VisitedIn) ->
        VisitedOut = VisitedIn;
        rb_insert(VisitedIn, Node, D1, VisitedOut)
    ),
    D2 is D1 + 1,
    findall(N, call(Np, Node, N), Neighbors),
    insert_neighbors(Neighbors, D2, VisitedOut, NextIn, NextOut),
    shortest_path(Np, Finish, FrontierOut, NextOut, VisitedOut, Length).

insert_neighbors([], _, _, T, T).
insert_neighbors([X|Xs], Val, Visited, Tin, Tout) :-
    (rb_lookup(X, _, Visited) ->
        Tin2 = Tin;
        rb_insert(Tin, X, Val, Tin2)
    ),
    insert_neighbors(Xs, Val, Visited, Tin2, Tout).

