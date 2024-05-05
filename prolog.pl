# monkey banana
% Define the possible moves and their effects on states
move(state(middle, onbox, middle, hasnot), grasp, state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H), drag(P1, P2), state(P2, onfloor, P2, H)) :-
    \+ P1 = P2. % Ensure that P1 and P2 are different positions.
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)) :-
    can_walk(P1, P2).

% Define the possible positions to walk from and to
can_walk(middle, left).
can_walk(middle, right).
can_walk(left, middle).
can_walk(right, middle).

% Define when the monkey can get the banana
canget(state(_, _, _, has)).

% Define when the monkey can get the banana by performing moves recursively
canget(State1) :-
    move(State1, _, State2),
    canget(State2).

% Example query to find out if the monkey can get the banana
% ?- canget(state(middle, onfloor, middle, hasnot)).


# easy monkey banana
% Initial state
at(monkey, door).
at(box, middle).
at(chair, middle).
at(banana, ceiling).

% Define the actions the monkey can take
move(monkey, door, middle).
move(monkey, middle, door).
move(monkey, middle, box).
move(monkey, middle, chair).
move(monkey, box, middle).
move(monkey, chair, middle).

% Rules for taking the banana
can_take(monkey, banana) :-
    at(monkey, X),
    at(banana, X).

% Define the goal state
goal_state :-
    can_take(monkey, banana).

% Define a predicate to solve the problem
solve :-
    goal_state,
    write('Monkey has taken the banana!'), nl.

solve :-
    move(Object, From, To),
    retract(at(Object, From)),
    assert(at(Object, To)),
    write(Object), write(' moved from '), write(From), write(' to '), write(To), nl,
    solve.


# celcius to farenheit conversion
celsius_to_fahrenheit(Celsius, Fahrenheit) :-
    Fahrenheit is (Celsius * 9/5) + 32.

# fibonacci series
% Factorial predicate
factorial(0, 1). % Base case: factorial of 0 is 1
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% Fibonacci predicate
fibonacci(0, 0). % Base case: Fibonacci of 0 is 0
fibonacci(1, 1). % Base case: Fibonacci of 1 is 1
fibonacci(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2.


# travelling salesman
% Define cities
city(a).
city(b).
city(c).
city(d).

% Define distances between cities
distance(a, b, 10).
distance(a, c, 15).
distance(a, d, 20).
distance(b, c, 35).
distance(b, d, 25).
distance(c, d, 30).

% Define permutation predicate to generate all possible permutations
permutation([], []).
permutation(List, [H|Perm]) :-
    select(H, List, Rest),
    permutation(Rest, Perm).

% Calculate total distance of a path
total_distance(Path, TotalDistance) :-
    append(Path, [FirstCity], PathWithFirst),
    append([LastCity], PathWithFirst, Path),
    distance_sum(Path, 0, TotalDistance).

distance_sum([_], TotalDistance, TotalDistance).
distance_sum([City1, City2|Rest], Acc, TotalDistance) :-
    distance(City1, City2, Distance),
    NewAcc is Acc + Distance,
    distance_sum([City2|Rest], NewAcc, TotalDistance).

% Find the shortest path
shortest_path(ShortestPath, ShortestDistance) :-
    findall(Path, permutation([a, b, c, d], Path), AllPaths),
    findall(Distance, (member(Path, AllPaths), total_distance(Path, Distance)), Distances),
    min_list(Distances, ShortestDistance),
    member(ShortestPath, AllPaths),
    total_distance(ShortestPath, ShortestDistance).

% Example usage:
% ?- shortest_path(Path, Distance).


# family relations
% Define family relationships
parent(alice, bob).
parent(alice, carol).
parent(carol, david).
parent(carol, eve).
parent(eve, frank).

% Define gender
male(bob).
male(david).
male(frank).
female(alice).
female(carol).
female(eve).

% Define rules for different relationships
father(Father, Child) :- parent(Father, Child), male(Father).
mother(Mother, Child) :- parent(Mother, Child), female(Mother).
child(Child, Parent) :- parent(Parent, Child).
sibling(Sibling1, Sibling2) :- parent(Parent, Sibling1), parent(Parent, Sibling2), Sibling1 \= Sibling2.

% Query examples
%?- father(bob, carol). % Bob is the father of Carol.
%?- sibling(bob, carol). % Bob and Carol are siblings.
%?- mother(Mother, david). % Who is the mother of David?
