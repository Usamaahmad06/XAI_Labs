#include <incmode>.


#program base.

rock(0..4).
cell((0..10,0..10)).

good(0).
good(1).

loc(0, (2,5)).
loc(1, (5,2)).
loc(2, (8,6)).
loc(3, (1,9)).

at((0,0), 1). %location (0,0) at time 1


#program step(t).
% Exactly one action per time step
1 { east(t); north(t); south(t); west(t); sample(R,t) : rock(R) } 1.

% Sampled rocks persist
sampled(R,t) :- sample(R,t).
sampled(R,t) :- sampled(R,t-1), rock(R).

% Movement effects
at((X+1,Y),t) :- east(t), at((X,Y),t-1), cell((X+1,Y)).
at((X-1,Y),t) :- west(t), at((X,Y),t-1), cell((X-1,Y)).
at((X,Y+1),t) :- north(t), at((X,Y),t-1), cell((X,Y+1)).
at((X,Y-1),t) :- south(t), at((X,Y),t-1), cell((X,Y-1)).

% Sampling keeps the agent on the rock cell
at(L,t) :- sample(R,t), loc(R,L), at(L,t-1).

% Preconditions (aggregates / integrity constraints)
:- east(t), at((X,Y),t-1), not cell((X+1,Y)).
:- west(t), at((X,Y),t-1), not cell((X-1,Y)).
:- north(t), at((X,Y),t-1), not cell((X,Y+1)).
:- south(t), at((X,Y),t-1), not cell((X,Y-1)).
:- sample(R,t), loc(R,L), not at(L,t-1).
:- sample(R,t), sampled(R,t-1).

% Exactly one position at each time step
:- not 1 { at(C,t) : cell(C) } 1.

#program check(t).
%:- query(t), t<2. %debug purpose
:- query(t), not sampled(R,t), rock(R), good(R). %all good rocks must be sampled



#show east/1.
#show south/1.
#show north/1.
#show west/1.
#show sample/2.
%#show at/2.
