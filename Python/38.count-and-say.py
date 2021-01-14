#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def generator(strin):
            res = []
            last_char = strin[0]
            count_last_char = 1
            for i in range(1, len(strin)):
                if strin[i] != last_char:
                    res.append(str(count_last_char))
                    res.append(last_char)
                    count_last_char = 1
                    last_char = strin[i]
                elif strin[i] == last_char:
                    count_last_char += 1
            res.append(str(count_last_char))
            res.append(last_char)
            return "".join(res)

        if n == 1:
            return "1"
        return generator(self.countAndSay(n-1)) 
        
# @lc code=end

