#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sub = []
        for i,v in enumerate(s):
            if v not in sub:
                sub.append(v)
                res = max(res, len(sub))
            else:
                cur_v_i = sub.index(v)
                sub = sub[cur_v_i+1:]
                sub.append(v)
        return res

        
# @lc code=end

