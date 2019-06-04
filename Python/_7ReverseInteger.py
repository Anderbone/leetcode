class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        flag = False
        num = x
        if x < 0:
            flag = True
            num = abs(x)
        print(num)
        while(num!=0):
            ans *= 10
            ans += int(num % 10)
            num = int(num/10)
            print (ans)
        print(ans)
        try:
            text = int(ans)
            if flag == True:
                return text*(-1)
            else:
                return text
        except:
            return 0

    def reverse2(self, x: int) -> int:
        if (x<-2**31 or x>2**31-1):
            print('saf')
            return 0
        ans = 0
        flag = False
        num = x
        if x < 0:
            flag = True
            num = abs(x)
        while(num!=0):
            ans *= 10
            ans += int(num % 10)
            num = int(num/10)
        print(ans)

        if flag == True:
            return ans*(-1)
        else:
            return ans

if __name__ == "__main__":
    s = Solution()
    a = s.reverse2(123)
    print(a)