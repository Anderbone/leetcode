#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        a = format(n,"032b")
        return int(a[::-1],2)


        
# @lc code=end

