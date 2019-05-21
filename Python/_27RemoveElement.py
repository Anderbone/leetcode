from typing import List
'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = 0
        for count, i in enumerate(nums):
            if i == val:
                continue
            else:
                nums[k] = nums[count] 
                k = k+1
        return k
                

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        while (1):
            try:
                nums.remove(val)
            except:
                return len (nums)


if __name__ == "__main__":
    s = Solution2()
    ans = s.removeElement([1,2,2,3,4],2)
    print(ans)