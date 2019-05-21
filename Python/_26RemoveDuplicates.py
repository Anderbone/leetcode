from typing import List
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return 1
        for count, i in enumerate(nums):
            j = count+1
            if j == len(nums):
                print(nums)
                return len(nums)
            while i == nums[j]:
                nums.remove(i)
                # j = j+1
                if j == len(nums):
                    print(nums)
                    return len(nums)
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        left = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != nums[left]:
                left+=1
                nums[left] = nums[i]
        return left + 1


if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    a = s.removeDuplicates(nums)
    print('hhhhh'+str(a))