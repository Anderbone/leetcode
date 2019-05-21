from typing import List
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
       
    def rotate2(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0,nums.pop())

        # other:
        #  k = k % len(nums)
        #  nums[:] = nums[-k:] + nums[:-k]

        # nums.reverse()
        # k = k % len(nums)  
        # nums[:k]=nums[:k][::-1] # [7,6,5] -> [5,6,7]
        # nums[k:]=nums[k:][::-1] #[4,3,2,1] -> [1,2,3,4]

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate2(nums,3)
    print('hhe')
    print(nums)
    # print('hhhhh'+str(a))