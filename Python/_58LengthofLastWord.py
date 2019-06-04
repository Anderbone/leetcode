class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" :
            return 0
        list  = s.strip().split(' ')
        return len(list[-1])



if __name__ == "__main__":
    s = Solution()
    a = s.lengthOfLastWord('a ')
    print(a)