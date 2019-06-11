import itertools
from typing import List
import collections

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        def check(each):
            # stack = collections.deque()
            stack = []
            for i in each:
                if i == '(':
                    stack.append(i)
                elif i == ')':
                    # print(stack)
                    if not stack:
                        return False
                    elif stack.pop() != '(':
                        return False
            if not stack:
                return True
            return False

        out = list(itertools.product('()', repeat = n))
        # print(out)
        ans = []
        # print(out)
        for each in out:
            # print(type(each))
            s = ''
            for i in each:
                s += i
            if s.count('(') != s.count(')'):
                continue
            if check(s) is True:
                # print(s)
                ans.append(s)

        return ans


if __name__ == '__main__':
    s = Solution()
    a = s.generateParenthesis(6)
    for i in a:
        print(i)
