'''
    Problem: You are given a string s and an array of strings words. All the strings of words are of the same length.

    A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
    Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
'''

# Given a string and a list of words return a solution to it.
# We use a dictionary to store the words and their counts, and then we use a sliding window to check
# if the words in the window are in the dictionary and if they are, we check if the count of the word
# is greater than 0. If it is, we decrement the count of the word by 1. If the count of the word is 0,
# we return False
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        m = len(words[0])
        word_dict = dict()
        for w in words:
            if w not in word_dict:
                word_dict[w]=1
            else:
                word_dict[w]+=1
        # print(word_dict)
        
        def isCheck(sub, word_dict):
            w_dict = word_dict.copy()
            for i in range(n):
                w = sub[i*m:(i+1)*m]
                # print(w)
                if w not in w_dict:
                    return False
                else:
                    if w_dict[w] == 0:
                        return False
                    else:
                        w_dict[w] -= 1
            return True
        
        output = []
        for i in range(len(s)):
            if i+m*n <= len(s):
                # print(s[i:i+m*n], word_dict)
                if isCheck(s[i:i+m*n], word_dict):
                    output.append(i)
        return output
