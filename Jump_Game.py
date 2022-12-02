'''
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible_target = 0
        curr_pos = 0
        while curr_pos <= possible_target:
            # if curr_pos + nums[curr_pos] > possible_target:
            possible_target = max(curr_pos + nums[curr_pos], possible_target)
            if possible_target >= len(nums)-1:
                return True
            curr_pos += 1
        return False