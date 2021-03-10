#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next is None or head.next.next is None:
            return head
        
        flag = 1
        head1 = pre = head
        l2 = ListNode(head.next.val) 
        head2 = l2
        pre = pre.next.next
            
        while (pre is not None):
            if flag == 1:
                head1.next = pre
                pre = pre.next
                head1 = head1.next
                flag = 0
              
            elif flag == 0:
                head2.next = pre
                pre = pre.next
                head2 = head2.next
                flag = 1
          
        head1.next = l2
        head2.next = None
        
        return head

# @lc code=end

