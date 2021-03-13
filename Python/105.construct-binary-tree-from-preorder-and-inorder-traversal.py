#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        d=len(inorder)-1
        i,j=0,d
        preorder.reverse()
        map_inorder={val:index for index,val in enumerate(inorder)}
        def recur(low,high):
            if low>high:
                return None
            root = TreeNode(preorder.pop())
            mid = map_inorder[root.val]
            root.left = recur(low,mid-1)
            root.right = recur(mid+1,high)
            return root

        return recur(0,d)

# @lc code=end

