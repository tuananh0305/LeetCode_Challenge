'''
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Constraints:
1 <= n <= 104
'''

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for x in range(1,N+1):
            has2569 = False
            has347 = False
            while (x>0):
                tmp = x%10
                x = x / 10
                if (tmp == 3 or tmp == 4 or tmp ==7):
                    has347 = True
                if (tmp == 2 or tmp == 5 or tmp ==6 or tmp ==9):
                    has2569 = True
            if (has347 == True):
                continue
            else:
                if (has2569 == False):
                    continue
                else:
                    count = count + 1
        return(count)
        