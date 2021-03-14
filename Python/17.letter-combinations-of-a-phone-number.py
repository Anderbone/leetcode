#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backTracking(digits, carry):
            if digits == []:
                res.append(carry)
                return

            number = digits[0]
            for j in dic[number]:
                backTracking(digits[1:], carry + j)
                 
        if not digits:
            return []
        digits = list(digits)
        res = []
        dic = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        backTracking(digits, '')
        return res


        
# @lc code=end

