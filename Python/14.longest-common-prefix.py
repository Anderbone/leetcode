#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        common = strs[0]
        index = len(common)
        for i in strs[1:]:
            index = min(index, len(i))
            while (common[:index] != i[:index]):
                index -= 1
        return "" if index == -1 else common[:index]
        # print('hello')
        
# @lc code=end
s = Solution()
strs = ["flower", "flow", "flight"]
res = s.longestCommonPrefix(strs)
print(res)
