class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)+'*'   
        ans = ''
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                ans = ans+ str(count)+s[i]
                count = 1
        return ans
     

if __name__ == "__main__":
    s = Solution()
    a = s.countAndSay(5)
    print(a)