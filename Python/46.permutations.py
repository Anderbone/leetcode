#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, permutation, result):
            if nums == []:
                result.append(permutation)
            for i,x in enumerate(nums):
                dfs(nums[:i] + nums[i+1:], permutation + [x], result)
            
        result = []
        dfs(nums, [], result)
        return result
# @lc code=end

