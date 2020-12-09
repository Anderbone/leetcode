#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        read_pointer_1 = m - 1
        read_pointer_2 = n - 1
        write_pointer = m + n - 1
        while read_pointer_2 >= 0:
            if read_pointer_1 >= 0 and nums1[read_pointer_1] >= nums2[read_pointer_2]:
                nums1[write_pointer] = nums1[read_pointer_1]
                read_pointer_1 -= 1
            else:
                nums1[write_pointer] = nums2[read_pointer_2]
                read_pointer_2 -= 1
            write_pointer -= 1
        
# @lc code=end

