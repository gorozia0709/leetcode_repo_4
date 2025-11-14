class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
   
    INT_MIN, INT_MAX = -2147483648, 2147483647
    
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1   # i = i * 2
            temp <<= 1 # temp = temp * 2
            
    if not positive:
        res = -res
        
    return res