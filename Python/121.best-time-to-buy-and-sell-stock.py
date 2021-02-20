#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minday = prices[0]
        maxprofit = 0
        for v in prices:
            if v < minday:
                minday = v
            else:
                maxprofit = max(maxprofit, v - minday)

        return maxprofit
        
# @lc code=end

