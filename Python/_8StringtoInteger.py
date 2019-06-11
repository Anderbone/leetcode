from re import compile
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_VALUE, MAX_VALUE = - 2 ** 31, 2 ** 31 - 1
        pattern = compile(r'^ *([\+-]?\d+){1}')
        matched = pattern.match(s)
        print(matched)
        print(matched.group())
        if matched:
            return min(MAX_VALUE, max(MIN_VALUE, int(matched.group())))
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    ans = s.myAtoi('-3+2+22-1  a')
    print(ans)