#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(temp, left, right):
            if len(temp) == 2 * n:
                ans.append(temp)
            if left < n:
                backtracking(temp+'(', left+1, right)
            if right < left:
                backtracking(temp+')', left, right+1)

        ans = []
        backtracking('', 0, 0)
        return ans


# @lc code=end

