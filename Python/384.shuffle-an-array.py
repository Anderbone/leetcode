#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.origin[:]
        random.shuffle(nums)
        return nums
        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

