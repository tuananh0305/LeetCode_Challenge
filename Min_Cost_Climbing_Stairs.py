'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost_to_reach = [0] * (len(cost)+1)
        for i in range(2,len(cost)+1):
            min_cost_to_reach[i] = min(min_cost_to_reach[i-1] + cost[i-1], min_cost_to_reach[i-2] + cost[i-2])
        return(min_cost_to_reach[len(cost)])
        
        