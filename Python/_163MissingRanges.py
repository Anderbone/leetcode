class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        res = []
        if not nums:
            res.append([lower,upper])
        else:
            if nums[0]>lower:
                res.append([lower,nums[0]-1])
            # nums.append(upper)
            for i,v in enumerate(nums):
                if i == len(nums)-1:
                    break
                if v+1 == nums[i+1] or v == nums[i+1]:
                    continue
                else:
                    res.append([v+1, nums[i+1]-1])
            if nums[-1]<upper:
                res.append([nums[-1]+1, upper])

        ans = []
        for i in res:
            if i[0]==i[1]:
                ans.append(str(i[0]))
            else:
                ans.append(str(i[0])+'->'+str(i[1]))

        return ans

inp = [0,1,3,50,75]
lower = 0
upper = 99
s = Solution()
r = s.findMissingRanges(inp, lower, upper)
print(r)




