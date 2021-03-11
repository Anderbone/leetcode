#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        
        lena = getLength(headA)
        lenb = getLength(headB)
        if lena < lenb:
            headA, headB = headB, headA
        diff = getLength(headA) - getLength(headB)
        while diff:
            headA = headA.next
            diff -= 1
            
        if not headA or not headB:
            return None
        
        while headA != headB:
            headA, headB = headA.next, headB.next

        return headA




        
# @lc code=end

