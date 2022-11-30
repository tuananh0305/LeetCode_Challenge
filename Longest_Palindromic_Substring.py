'''
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution(object):
    def isPalindromic(self, s):
        palindromic_s = s[::-1]
        return (s == palindromic_s)
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        result_s = ''
        max_s = 0
        
        for i in range(length):
            for j in range(i, length):
                sub_s = s[i:j+1]
                if ((len(sub_s) > max_s) and self.isPalindromic(sub_s)):
                    if (len(sub_s) > max_s):
                        max_s = len(sub_s)
                        result_s = sub_s
        return(result_s)
                
