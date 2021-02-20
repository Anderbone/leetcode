#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        profit = {0: nums[0], 1: max(nums[0], nums[1])}
        for i in range(2, len(nums)):
            profit[i] = max(profit[i-2]+nums[i], profit[i-1])
        return profit[len(nums)-1]





        
# @lc code=end

