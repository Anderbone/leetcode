#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Return True if subarray
        # board[start_row:end_row][start_col:end_col] contains any
        # duplicates in {1, 2, ..., len(board)}; otherwise return
        # False.
        def has_duplicate(block):
            block = list(filter(lambda x: x != '.', block))
            return len(block) != len(set(block))

        n = len(board)
        # Check row and column constraints.
        if any(
                has_duplicate([board[i][j] for j in range(n)])
                or has_duplicate([board[j][i] for j in range(n)])
                for i in range(n)):
            return False

        # Check region constraints.
        region_size = int(math.sqrt(n))
        return all(not has_duplicate([
            board[a][b]
            for a in range(region_size * I, region_size * (I + 1))
            for b in range(region_size * J, region_size * (J + 1))
        ]) for I in range(region_size) for J in range(region_size))



        
# @lc code=end