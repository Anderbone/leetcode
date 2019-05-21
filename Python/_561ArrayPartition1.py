from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0   
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            total += nums[i]
        return total


if __name__ == "__main__":
    s = Solution()
    ans = s.arrayPairSum([1,2,3,4])
    print(ans)