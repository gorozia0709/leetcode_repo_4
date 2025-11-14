class Solution:
  def myAtoi(self, s: str) -> int:
    state = 0
    result = 0
    sign = 1
    
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    for char in s:
      if state == 0:
        if char == ' ':
          continue
        elif char == '+':
          state = 1
        elif char == '-':
          sign = -1
          state = 1
        elif char.isdigit():
          result = int(char)
          state = 2
        else:
          break
      elif state == 1:
        if char.isdigit():
          result = int(char)
          state = 2
        else:
          break
      elif state == 2:
        if char.isdigit():
          if result > (INT_MAX - int(char)) // 10:
            return INT_MAX if sign == 1 else INT_MIN
          result = result * 10 + int(char)
        else:
          break
          
    return result * sign