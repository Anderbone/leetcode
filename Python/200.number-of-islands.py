#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #The trick here is to see a one and then invert all surrounding 1's to 0's so we do not do redudant computations.
        if len(grid) is 0: return 0 
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0 
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] is '1':
                    islands += 1
                    self.dfs(grid, row, col)
                    
        return islands
    
    def dfs(self, board, row, col):
        if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])) or (board[row][col] is '0'): 
            return 
        
        board[row][col] = '0'
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)
        
        return

# @lc code=end

