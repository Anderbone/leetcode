import collections

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

    def firstUniqChar3(self, s: str) -> int:
        if not s:
            return -1
        dic = {}
        for i in s:
            try:
                v = dic[i]
                dic[i] = v+1
            except:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                return s.index(i)
        return -1

    def firstUniqChar4(self, s):
        if not s:
            return -1
        dic = collections.defaultdict(lambda: 0)
        for i in s:
            dic[i] += 1

        for i in dic:
            if dic[i] == 1:
                return s.index(i)
        return -1