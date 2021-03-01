#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        while x or y:
            dis += (x&1) ^ (y&1)
            x >>= 1
            y >>= 1
        return dis
        
# @lc code=end

