#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = head = ListNode(0)
        while l1 or l2:
            num1 = num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            summ = num1 + num2 + carry
            carry = summ // 10
            cur = summ % 10
            head.next = ListNode(cur)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return res.next






        

        
# @lc code=end

