class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        end = nums[0]
        if len(nums) == 1:
            return m
        for i in nums[1:]:
            end = max(i, end+i)
            m = max(end,m)
        return m