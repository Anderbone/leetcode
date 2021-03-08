#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        seq = []
        
        for num in nums:
            if not seq or num > seq[-1]:
                seq.append(num)
                if len(seq) == 3:
                    return True
            elif num <= seq[0]:
                seq[0] = num
            elif num <= seq[1]:
                seq[1] = num      

        return False

        
# @lc code=end

