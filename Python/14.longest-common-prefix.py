#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
        # print('hello')
        
# @lc code=end
s = Solution()
strs = ["flower", "flow", "flight"]
res = s.longestCommonPrefix(strs)
print(res)
