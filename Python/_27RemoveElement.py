from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = 0
        for count, i in enumerate(nums):
            if i == val:
                continue
            else:
                nums[k] = nums[count] 
                k = k+1
        return k
                

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        while (1):
            try:
                nums.remove(val)
            except:
                return len (nums)


if __name__ == "__main__":
    s = Solution2()
    ans = s.removeElement([1,2,2,3,4],2)
    print(ans)