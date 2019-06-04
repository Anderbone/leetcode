class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split(' ')
        while ("" in l):
            l.remove('')
        l.reverse()
        return  " ".join(l)