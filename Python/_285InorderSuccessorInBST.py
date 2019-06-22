"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        all = []

        def help(root):
            if not root:
                return
            help(root.left)
            all.append(root)
            help(root.right)
        help(root)

        for i,v in enumerate(all):
            if i == len(all)-1:
                return None
            elif v == p:
                return all[i+1]




