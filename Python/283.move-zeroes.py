#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero_count = i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.remove(nums[i])
        #         zero_count += 1
        #         i -= 1
        #     i += 1


        # nums.extend([0] * zero_count)
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))

        index_not_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index_not_zero] = nums[index_not_zero], nums[i]
                index_not_zero += 1


            
        
# @lc code=end

