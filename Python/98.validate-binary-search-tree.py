#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # inorder traversal, then compare with sorted
        num = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            num.append(root.val)
            inorder(root.right)
        inorder(root)
        if len(set(num)) != len(num):
            return False
        if sorted(num) == num:
            return True
        return False

            

        
# @lc code=end

