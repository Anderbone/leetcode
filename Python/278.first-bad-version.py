#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin, end = 1, n
        while begin < end:
            mid = (begin + end) // 2

            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1

        return end
        
        
# @lc code=end
