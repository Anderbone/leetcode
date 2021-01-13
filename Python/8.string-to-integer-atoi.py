#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        purenum = []
        start_positive = False
        negative = False
        for v in s:
            if not purenum:
                if v == ' ':
                    if negative or start_positive:
                        return 0
                    continue
                elif v == "+":
                    if negative or start_positive:
                        return 0
                    start_positive = True
                    continue
                elif v == '-':
                    if start_positive or negative:
                        return 0
                    negative = True
                elif not v.isdigit():
                    return 0
            
            if v.isdigit():
                purenum.append(v)
            else:
                if purenum:
                    break

        if not purenum:
            return 0
        
        num = int("".join(purenum))
        if negative:
            return -2**31 if num > 2**31 else num * -1
        return 2**31-1 if num > 2**31-1 else num
        
        
        
            

        
# @lc code=end

