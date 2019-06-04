from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # l = []
        # for i in digits:
        #     l.append([i])
        s = "".join(str(i) for i in digits)
        num = int(s)
        ans = num+1
        s = str(ans)
        final = []
        for i in list(s):
            final.append(int(i))
        return final

if __name__ == "__main__":
    s = Solution()
    a= s.plusOne([1,2,9])
    print(a)