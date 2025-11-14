class Solution:
  def solveNQueens(self, n: int) -> list[list[str]]:
    result = []
    queens_pos = [-1] * n
    occupied_cols = set()
    occupied_pos_diagonals = set()
    occupied_neg_diagonals = set()

    def backtrack(row):
      if row == n:
        board = []
        for r in range(n):
          line = ['.'] * n
          line[queens_pos[r]] = 'Q'
          board.append("".join(line))
        result.append(board)
        return

      for col in range(n):
        if (col not in occupied_cols and
            (row + col) not in occupied_pos_diagonals and
            (row - col) not in occupied_neg_diagonals):
          
          queens_pos[row] = col
          occupied_cols.add(col)
          occupied_pos_diagonals.add(row + col)
          occupied_neg_diagonals.add(row - col)

          backtrack(row + 1)

          occupied_cols.remove(col)
          occupied_pos_diagonals.remove(row + col)
          occupied_neg_diagonals.remove(row - col)

    backtrack(0)
    return result