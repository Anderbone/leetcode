#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        return leng * (leng+1) // 2 - sum(nums)
        
# @lc code=end

