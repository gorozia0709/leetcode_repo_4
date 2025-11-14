class Solution:
  def reverse(self, x: int) -> int:
    s = str(x)
    reversed_s = ""
    
    if s[0] == '-':
      reversed_s = "-" + s[1:][::-1]
    else:
      reversed_s = s[::-1]
      
    num = int(reversed_s)
    
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if num < INT_MIN or num > INT_MAX:
      return 0
      
    return num
