# Technical Challenge 6
This is relevant for students that are in their first or second year of Bachelor's degree.

## Minesweeper
Minesweeper is a game where you see a grid of grey squares in the beginning. Hidden below the gray squares are mines (marked by a 9). Around each mine, there are 8 ones. If multiple mines are next to each other, the ones add up. The rest of the playing field has zeros in it.

If you click on a zero, the entire segment of zeroes and all the neighbours are revealed. If you click on a 9, you lose. If you click on any other number, only that field is revealed.

### Example
```0 0 0 0 0
0 0 0 0 0
1 1 1 0 0
1 X 1 0 0
1 2 2 1 0
0 1 X 1 0
0 1 1 1 0```

For example, if you click on the top right corner you get this ("-" means hidden):

```0 0 0 0 0
0 0 0 0 0
1 1 1 0 0
- - 1 0 0
- - 2 1 0
- - - 1 0
- - - 1 0```

Please write functions to:

1. Given the size and number of mines, construct the playing field.
2. Implement the "OnClick()" function.
3. Implement the "Print(bool show_hidden)" function. The Print(false) function returns a string representation of the current playing field state. All cells that are still hidden should be represented by '-'. A mine should be represented by 'X'. All visible cells should be represented by their current number. When the parameter show_hidden is true, Print(true)should return a string representation of the playing field with all the cells visible.

