# calcudoku-project
This is a repository of the files for the calcudoku game project I was assigned in my computer science class during my first year at Cal Poly SLO. The game involves an input from the user (written information) and an output in the form of a solved calcudoku grid. 

There are two parts to the program input. One is the set of instructions the code follows and the other is user input and both are outlined below.


User Input:

The user input involve two items of information: the first is the number of cages in the grid (a collection of cells in the grid grouped together and are meant to equal a particular sum) and the second is also split into two parts. The two parts are the total sum of all the numbers in a particular cage and the position of the cells included in each cage (begins from zero at the top right corner of the grid and increments by one as it moves cell by cell down each row, so the last cell will be n * n - 1). An example of the first line and the first info given for a cage by user input, given that the grid is 5 X 5, would be:

9
6 4 9 14

What we know from the info given is that the grid has a total of 9 cages that split up the 25 cells in the 5 by 5 grid. The first cage has the total sum of 6, has 3 cell, and those cells are positioned in the last cell on the right of the first, second, and third rows.


Instructions:

Calcudoku is similar in fashion to sudoku, but has a slightly stricter set of rules.Below is the instruction set my program adheres to solve the game.

Given an empty n X n grid, solving a grid would be defined as having filled an entire empty grid. In order to solve an empty grid, follow the rules below while filling it out:

- Each row and column must only use numbers 1 - n to fill the grid
- No two numbers may repeat in a single column or row, therefore each number 1 - n may only be used once

----------------------------------------------------------------------------------------------------------------------------

Here is a full example of input and output of this program:

Input:

Please enter the number of cages: 9
Cage number 0: 5 0 5
Cage number 1: 8 1 2 6
Cage number 2: 8 3 8
Cage number 3: 6 4 9 14
Cage number 4: 13 7 12 13
Cage number 5: 5 10 15
Cage number 6: 14 11 16 20 21
Cage number 7: 6 17 18 22
Cage number 8: 10 19 23 24


Output:

---Solution---

4 1 2 5 3 
1 5 4 3 2 
2 3 5 4 1 
3 4 1 2 5 
5 2 3 1 4 


checks: 2265 backtracks: 438


