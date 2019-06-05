import copy
class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            oldres = copy.deepcopy(res)
            print(oldres)
            for j in res:
                print(j)
                j.append(i)
            oldres = oldres + res
            res = oldres
            # print(oldres)
        return res



if __name__ == "__main__":
    s = Solution()
    a = s.subsets([1,2,3])
    print(a)
