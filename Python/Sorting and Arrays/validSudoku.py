'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        grid = {(x, y): set() for x in range(3) for y in range(3)}

        for i in range(len(board)):
            for j in range(len(row)):
                num = board[i][j]
                if num != ".":
                    # check row
                    if num in row[i]: return False
                    row[i].add(num)
                    # check column
                    if num in column[j]: return False
                    column[j].add(num)
                    # check 3x3 grid
                    x = i // 3
                    y = j // 3
                    if num in grid.get((x, y)): return False
                    grid[(x, y)].add(num)

        return True






