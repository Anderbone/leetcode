#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = dict(collections.Counter(s))
        dic_t = dict(collections.Counter(t))
        return dic_s == dic_t
        
# @lc code=end

