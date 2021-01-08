#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_values = {}
        for i, v in enumerate(nums):
            need_value = target - v
            if need_value in need_values:
                return [need_values[need_value], i]
            else:
                need_values[v] = i

# @lc code=end

