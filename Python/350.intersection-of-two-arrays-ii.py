#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count1 = dict(collections.Counter(nums1))
        count2 = dict(collections.Counter(nums2))
        for v in count1:
            if v in count2:
                num_v = min(count1[v], count2[v])
                res.extend(num_v * [v])
        return res

        
# @lc code=end

