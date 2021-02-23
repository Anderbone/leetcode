#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # list comprehension with string rule of FizzBuzz
        list_of_output = [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]
        
        return list_of_output

        
# @lc code=end

