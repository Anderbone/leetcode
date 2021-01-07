#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # use -k or use len(nums)-k, can't use both in a same line.
        nums[:] = nums[-k:] + nums[:-k]

# @lc code=end

