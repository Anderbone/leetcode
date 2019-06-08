import collections


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = collections.deque()
        for i in s:
            if i is '(' or i is '{' or i is '[':
                stack.append(i)
            elif i is '}' or i is ')' or i is ']':
                if not stack:
                    return False
                if dic[stack.pop()] is not i:
                    return False

        if not stack:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    ans = s.isValid('(]')
    print(ans)
