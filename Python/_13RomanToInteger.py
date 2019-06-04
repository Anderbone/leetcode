class Solution:

    def romanToInt(self, s: str) -> int:
        mapping = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
        }
        if not s:
            return 0
        sum = 0
        slist = list(s)
        for i,letter in enumerate(slist):
            # print(i)
            # print(letter)
            if i == len(s)-1:
                break
            first = letter
            second = slist[i+1]
            if mapping[letter]< mapping[second]:
                sum-=mapping[letter]
            else:
                sum+=mapping[letter]
        return sum+mapping[s[-1]]


if __name__ == "__main__":
    s = Solution()
    ans = s.romanToInt('MDC')
    print(ans)