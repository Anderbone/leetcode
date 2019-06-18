class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        diclist = {}
        for ss in strs:
            print(ss)
            print(sorted(ss))
            temp = ''.join(sorted(ss))
            print(temp)
            if temp in diclist:
                diclist[temp].append(ss)
            else:
                diclist[temp] = [ss]
        return [diclist[i] for i in diclist]


s = Solution()
inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
o = s.groupAnagrams(inp)
print(o)

