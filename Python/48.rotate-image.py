#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1

        for i in range(len(matrix) // 2):
            for j in range(i, size - i):
                matrix[i][j], matrix[~j][i], matrix[~i][~j],matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

        
# @lc code=end

