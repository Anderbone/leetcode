'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
'''
from typing import List
import sys

class Solution:
    def firstMissingPositive(self, nums):
        i = 0
        while (i<len(nums)): 
            if nums[i]<=0: nums.pop(i)
            else: i+=1
        for i in range(len(nums)):
            index = nums[i]-1
            if index<len(nums) and nums[index]>0: nums[index] *= -1
        for i in range(len(nums)):
            if nums[i]>0: return i+1
        return len(nums)+1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, x in enumerate(nums):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

