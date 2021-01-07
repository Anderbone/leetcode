#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for v in nums:
            if v != nums[i]:
                i += 1
                nums[i] = v
        return i+1




# @lc code=end

