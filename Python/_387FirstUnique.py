class Solution:
    def firstUniqChar(self, s: str) -> int:
        # time limit exceed!
        if s == "":
            return -1
        l = list(s)
        point = l[0]
        while (True):
            if point not in l[1:]:
                return s.index(point) 
            else:
                while point in l:
                    l.remove(point)
                if len(l) == 0:
                    return -1
                point = l[0]
        return -1
        

    def firstUniqChar2(self, s: str) -> int:
        d = dict(collections.Counter(s))
        for each in d.keys():
            if d[each] == 1:
                return s.index(each)
        return -1
