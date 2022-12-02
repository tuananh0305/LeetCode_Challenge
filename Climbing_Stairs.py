'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Constraints:

1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # n=0 -> 1
        # n=1 -> (n=0) =  1
        # n=2 -> (n=1)+(n=0) = 2
        # n=3 -> (n=2)+(n=1) = 3
        if n==1:
            return 1
        elif n==2:
            return 2
        
        n_1 = 1
        n_2 = 2
        result = 0
        for i in range(n-2):
            result = n_1 + n_2
            n_1 = n_2
            n_2 = result
        return result