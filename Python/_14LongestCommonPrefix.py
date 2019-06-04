class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        j = len(strs[0])
        for i in range(len(strs)-1):
            first = strs[i]
            second = strs[i+1]
            while (first[:j] != second[:j]):
                j  -= 1
        return strs[0][:j]