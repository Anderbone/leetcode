#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        count = 0
        for num in range(2, n):
            if prime[num] == True:
                count += 1
                for i in range(num*num, n, num):
                    prime[i] = False
        return count

        

# @lc code=end

