package leetcode;
/*
 * #array #binary search
 * Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
Example 2:
Input: [1,3,5,6], 2
Output: 1

 */
public class _35_SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int i = 0;
    	while(target>nums[i]){
        	i++;
        	if(i==nums.length){
        		return i;
        	}
        }
        return i;
    }
    public static void main(String[] args) {
		int[] a = {1,3,5,6};
		System.out.println(searchInsert(a, 5));
		System.out.println(searchInsert(a, 2));
		System.out.println(searchInsert(a, 7));
		System.out.println(searchInsert(a, 0));
	}

}
