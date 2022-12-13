'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:     
        if (numRows == 1):
            return s
        
        arr = ["" for i in range(numRows)]
        LEN = len(s)
        numRepeat = (numRows-1) * 2
        for i in range(LEN):
            j = i%numRepeat
            if j>=numRows:
                j = numRepeat-j
            arr[j]+=s[i]
        # print(arr)
        out=""
        for i in range(numRows):
            out+=arr[i]
        return(out)

