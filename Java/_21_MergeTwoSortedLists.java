package leetcode;
/*
 * #linked list
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

 */

public class _21_MergeTwoSortedLists {

	
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	
    	ListNode ans = new ListNode(0);
    	ListNode pre = ans;
    	while(l1 != null || l2 != null){
    		if( l1 == null || (l2!=null)&&(l2.val <= l1.val)){
    			pre.next = l2;
   
    			l2 = l2.next;
    			pre = pre.next;
    		}else{
    			pre.next = l1;
    			l1 = l1.next;
    			pre = pre.next;
    			
    		}
    	}
    	return ans.next;    
    	
    }
    
    public static void main(String[] args) {
    	//MergeTwoSortedLists m = new MergeTwoSortedLists();
		ListNode n1 = new ListNode(1);
		ListNode n2 = new ListNode(2);
		ListNode n3 = new ListNode(4);
		n1.next = n2;
		n2.next = n3;
//		while(n1!=null){
//			System.out.print(n1.val);
//			n1 = n1.next;
//		}
//		System.out.println();
		
		ListNode b1 = new ListNode(1);
		ListNode b2 = new ListNode(3);
		ListNode b3 = new ListNode(4);
		b1.next = b2;
		b2.next = b3;
//		while(b1!=null){
//			System.out.print(b1.val);
//			b1 = b1.next;
//		}
//		System.out.println();
		ListNode ans = mergeTwoLists(n1, b1);
		while(ans!=null){
			System.out.println(ans.val);
			ans = ans.next;
		}
		
	}

	
}


