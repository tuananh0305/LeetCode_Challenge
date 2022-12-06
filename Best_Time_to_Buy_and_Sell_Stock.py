'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low_index = 0
        high_index = 0
        profit = 0
        for i in range(1,len(prices)):
            if (prices[i] > prices[high_index]):
                high_index = i
                if (prices[high_index] - prices[low_index] > profit):
                    profit = prices[high_index] - prices[low_index]
            if (prices[i] < prices[low_index]):
                low_index = i
                high_index = i
                
        return(profit)
