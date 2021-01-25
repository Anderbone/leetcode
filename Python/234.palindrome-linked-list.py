#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        quick = slowhead = head
        slowpassed = None

        while quick and quick.next:
            quick = quick.next.next
            slowhead = head
            head = head.next
            slowhead.next = slowpassed
            slowpassed = slowhead
        
        if quick:
            head = head.next
        
        while head and slowpassed:
            if head.val != slowpassed.val:
                return False
            slowpassed, head = slowpassed.next, head.next
        if head or slowpassed:
            return False
        return True
        
        # return slow == slowhead





        
# @lc code=end

