class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    matrix = [['' for _ in range(len(s))] for _ in range(numRows)]
    row, col = 0, 0
    direction = -1

    for char in s:
        matrix[row][col] = char
        if row == 0 or row == numRows - 1:
            direction *= -1
        
        if direction == 1:
            row += 1
        else:
            row -= 1
            col += 1
            
    result = ""
    for r in range(numRows):
        result += "".join(matrix[r])
        
    return result