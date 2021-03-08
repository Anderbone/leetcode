#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_ana = {}
        for word in strs:
            sword = "".join(sorted(word))
            if sword not in dic_ana:
                dic_ana[sword] = [word]
            else:
                dic_ana[sword].append(word)
        
        return [v for v in dic_ana.values()]

        
# @lc code=end

