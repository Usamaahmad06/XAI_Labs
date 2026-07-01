#include <incmode>.


#program base.

dist(0..24).
rock(0..4).
cell((0..11,0..11)).

% Learned rules from ILASP (Lab 4 assignment 1):
good(R) :- guess(R, V), V > 80.
good(R) :- dist(R, D, 1), D < 1.

% Manhattan distance from agent to rock at each timestep
dist(R, D, T) :- at((X, Y), T), loc(R, (Xr, Yr)), X >= Xr, Y >= Yr, D = (X - Xr) + (Y - Yr).
dist(R, D, T) :- at((X, Y), T), loc(R, (Xr, Yr)), X >= Xr, Y <  Yr, D = (X - Xr) + (Yr - Y).
dist(R, D, T) :- at((X, Y), T), loc(R, (Xr, Yr)), X <  Xr, Y >= Yr, D = (Xr - X) + (Y - Yr).
dist(R, D, T) :- at((X, Y), T), loc(R, (Xr, Yr)), X <  Xr, Y <  Yr, D = (Xr - X) + (Yr - Y).

loc(0, (2,2)).
loc(1, (5,2)).
loc(2, (2,4)).
loc(3, (9,9)).

at((0,0), 1).

guess(0,70).
guess(1,40).
guess(2,90).
guess(3,10).


#program step(t).
1 { east(t); north(t); south(t); west(t); sample(R,t) : rock(R) } 1.

sampled(R,t) :- sample(R,t).
sampled(R,t) :- sampled(R,t-1), rock(R).

at((X+1,Y),t) :- east(t), at((X,Y),t-1), cell((X+1,Y)).
at((X-1,Y),t) :- west(t), at((X,Y),t-1), cell((X-1,Y)).
at((X,Y+1),t) :- north(t), at((X,Y),t-1), cell((X,Y+1)).
at((X,Y-1),t) :- south(t), at((X,Y),t-1), cell((X,Y-1)).
at(L,t) :- sample(R,t), loc(R,L), at(L,t-1).

:- east(t), at((X,Y),t-1), not cell((X+1,Y)).
:- west(t), at((X,Y),t-1), not cell((X-1,Y)).
:- north(t), at((X,Y),t-1), not cell((X,Y+1)).
:- south(t), at((X,Y),t-1), not cell((X,Y-1)).
:- sample(R,t), loc(R,L), not at(L,t-1).
:- sample(R,t), sampled(R,t-1).
:- not 1 { at(C,t) : cell(C) } 1.


#program check(t).
:- query(t), not sampled(R,t), good(R).



#show east/1.
#show south/1.
#show north/1.
#show west/1.
#show sample/2.
%#show good/1.
%#show dist/2.
