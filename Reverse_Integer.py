'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        ix = 0
        if x>0:
            sign=1
        else:
            sign=-1
            x = -x
            
        while x>0:
            a = x%10
            ix = ix*10+a
            x=x//10
            
        ix = ix*sign
        if ix>=-2**31 and ix<=2**31-1:
            return ix
        else:
            return 0