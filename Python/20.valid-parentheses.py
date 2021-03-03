#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        par = {"(":")", "{":"}", "[":"]"}
        stack = []
        for v in s:
            if v in par:
                stack.append(v)
            else:
                if not stack or par[stack.pop()] != v:
                    return False
        return not stack        
# @lc code=end

