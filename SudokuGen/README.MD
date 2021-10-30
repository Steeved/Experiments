# Sudoku Generator
This is a python program that is used to generate a Sudoku in 3 difficulties: Easy, Normal, Hard.
## Usage:
To create a Sudoku run the program and after it starts it will prompt you
to enter one of the three possible difficulties (easy, normal, hard).

After running the program and selecting a difficulty, it should generate 
two files - `sudoku.txt` and `solution.txt`,
in the first one, it will write a unique sudoku and in the second file - its solution.
Every new start of this script will overwrite generated files.

Here's an example usage:

```bash
C:\Users\sbmar\Experiments\SudokuGen>python sudokuGen.py
Sudoku generator.
Available difficulties: easy,normal or hard
Difficulty: hard
```
Here's an example of generated files:

 * `sudoku.txt`
```text
[8][ ][ ][3][2][ ][4][ ][6]
[1][ ][4][ ][6][9][ ][ ][ ]
[2][5][ ][ ][ ][7][3][1][ ]
[ ][ ][5][9][ ][ ][6][ ][ ]
[ ][8][3][6][ ][ ][ ][9][4]
[ ][6][ ][4][ ][ ][8][ ][2]
[6][ ][9][ ][ ][ ][ ][2][3]
[ ][1][2][7][3][6][9][ ][ ]
[3][ ][8][2][ ][4][ ][6][5]
```
 * `solution.txt`
```text
[8][9][7][3][2][1][4][5][6]
[1][3][4][5][6][9][2][8][7]
[2][5][6][8][4][7][3][1][9]
[4][2][5][9][8][3][6][7][1]
[7][8][3][6][1][2][5][9][4]
[9][6][1][4][7][5][8][3][2]
[6][4][9][1][5][8][7][2][3]
[5][1][2][7][3][6][9][4][8]
[3][7][8][2][9][4][1][6][5]
```