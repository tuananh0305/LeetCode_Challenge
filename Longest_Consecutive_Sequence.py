'''
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        max_seq = 0
        for num in nums:
            if num-1 not in num_set:
                current_seq = 1
                x = num
                while x+1 in num_set:
                    x+=1
                    current_seq+=1
                max_seq = max(max_seq, current_seq)
        return max_seq