'''
Given a string s, find the length of the longest  substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        
        low=0
        out=1
                
        for high in range(1,len(s)):
            for i in range(low,high):
                if s[i]==s[high]:
                    low=i+1
                    break
            out=max(out, high-low+1)
            # print(low,high)
        return out