from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def traversal(root, level, res):
            if not root:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            traversal(root.left, level + 1, res)
            traversal(root.right, level + 1, res)

        res = [[]]
        traversal(root, 0, res)
        return res


if __name__ == '__main__':
    res = [[]]
    print(len(res))