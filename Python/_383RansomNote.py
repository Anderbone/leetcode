import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicr = dict(collections.Counter(ransomNote))
        dicm = dict(collections.Counter(magazine))
        for k in dicr.keys():
            if k not in magazine or dicr[k] > dicm[k]:
                return False
        return True
    