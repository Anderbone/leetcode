from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # for i in range(k): # time exceed
        #     last = nums[-1]
        #     for j in range(len(nums)-1,0,-1):
        #         nums[j] = nums[j-1]
        #     nums[0] = last
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