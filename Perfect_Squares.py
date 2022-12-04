'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Constraints:
1 <= n <= 104
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        N = int(round(sqrt(n)))
        squares = [x**2 for x in range(1,N+1)]
        out_list = [n]*(n+1)
        out_list[0] = 0
        for i in range(1,n+1):
            for j in squares:
                if i>=j and out_list[i-j]+1 < out_list[i]:
                    out_list[i] = out_list[i-j]+1
        return out_list[n]