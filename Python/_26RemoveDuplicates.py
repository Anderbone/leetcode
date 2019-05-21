from typing import List
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