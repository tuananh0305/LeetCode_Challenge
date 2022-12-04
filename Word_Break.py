'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False for i in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if len(w)<=i+1:
                    if s[i - len(w) + 1:i+1] == w:
                        if len(w)==i+1 or check[i - len(w)] == True:
                            check[i] = True
        print(check)
        return check[len(s)-1]