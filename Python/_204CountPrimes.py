class Solution:
    def countPrimes(self, n: int) -> int:
        Prime = [True]*n
        count = 0
        for i in range(2, n):
            if Prime[i]:
                count += 1
                for j in range(i*i,  n, i):
                    Prime[j] = False
        return count