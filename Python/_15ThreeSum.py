from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for cur_idx in range(len(nums)):
            if (cur_idx != 0) and (nums[cur_idx] == nums[cur_idx-1]):
                continue
            two_sum = -nums[cur_idx]
            left_idx = cur_idx + 1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                if nums[left_idx] + nums[right_idx] == two_sum:
                    res.append(
                        [nums[cur_idx], nums[left_idx], nums[right_idx]]
                    )
                    left_idx += 1
                    right_idx -= 1
                    while (left_idx < right_idx) and (nums[left_idx] == nums[left_idx-1]):
                        left_idx += 1
                    while (left_idx < right_idx) and (nums[right_idx] == nums[right_idx+1]):
                        right_idx -= 1
                elif nums[left_idx] + nums[right_idx] > two_sum:
                    right_idx -= 1
                else:
                    left_idx += 1
        return res


if __name__ == '__main__':
    n=3
    dp = [[0] * n for _ in range(n)]
    print(dp)
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))