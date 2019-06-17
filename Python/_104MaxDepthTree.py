class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        level = [root]; depth = 0
        while level:
            depth += 1
            level = [i for n in level for i in (n.left, n.right) if i]

            # level = []
            # for father in level:
            #     for new in father.left, father.right:
            #         if new:
            #             level.append[new]

        return depth


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth())