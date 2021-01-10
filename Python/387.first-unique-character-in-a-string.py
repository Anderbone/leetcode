#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = dict(collections.Counter(s))
        for char in char_count:
            if char_count[char] == 1:
                return s.index(char)
        return -1
        
# @lc code=end

