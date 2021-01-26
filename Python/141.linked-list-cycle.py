#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        quick = slow = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                return True
        return False
        
# @lc code=end

