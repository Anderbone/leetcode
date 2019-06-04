# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        pre = ans
        while(l1 != None or l2 != None):
            if (l1 == None or l2 != None) and (l2.val <= l1.val):
                pre.next = l2
                l2 = l2.next
                pre = pre.next
            else:
                pre.next = l1
                l1 = l1.next
                pre = pre.next
        return ans.next
