% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
subgrid(X, Y, 1) :- X = 1..3, Y = 1..3.
subgrid(X, Y, 2) :- X = 1..3, Y = 4..6.
subgrid(X, Y, 3) :- X = 1..3, Y = 7..9.
subgrid(X, Y, 4) :- X = 4..6, Y = 1..3.
subgrid(X, Y, 5) :- X = 4..6, Y = 4..6.
subgrid(X, Y, 6) :- X = 4..6, Y = 7..9.
subgrid(X, Y, 7) :- X = 7..9, Y = 1..3.
subgrid(X, Y, 8) :- X = 7..9, Y = 4..6.
subgrid(X, Y, 9) :- X = 7..9, Y = 7..9.
1 { sudoku(X, Y, N) : N = 1..9 } 1 :- X = 1..9, Y = 1..9.
:- sudoku(X, Y1, N), sudoku(X, Y2, N), Y1 != Y2.
:- sudoku(X1, Y, N), sudoku(X2, Y, N), X1 != X2.
:- sudoku(X1, Y1, N), sudoku(X2, Y2, N), subgrid(X1, Y1, G), subgrid(X2, Y2, G), X1 != X2, Y1 != Y2.
sudoku(X, Y, N) :- initial(X, Y, N).

#show sudoku/3.
