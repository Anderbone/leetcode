#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = list(i - j for i,j in zip(gas, cost)) * 2
        ans = cur = 0
        for i,v in enumerate(diff):
            cur += v
            if cur < 0:
                ans = i + 1
                cur = 0
                if i >= len(gas):
                    return -1
        return ans
        
# @lc code=end
s = Solution()
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# gas = [3,3,4]
# cost = [3,4,4]
gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
s.canCompleteCircuit(gas, cost)