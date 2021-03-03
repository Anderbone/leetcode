#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generate_next(lines):
            lastline = lines[-1]
            next = [1]
            for i in range(len(lastline)-1):
                next.append(lastline[i]+lastline[i+1])
            next.append(1)
            lines.append(next)
            return lines

        if numRows == 1:
            return [[1]] 
        return generate_next(self.generate(numRows-1))

        
# @lc code=end

