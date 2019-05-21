package leetcode;
/*
 * #27 误导人的描述。
 * #array #easy #two pointers
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
 */

public class _27_RemoveElement {
    static int removeElement(int[] nums, int val) {
    	int r = 0;
    	for(int i=0; i<nums.length; i++){
    		if(nums[i] != val){
    			nums[r] = nums[i];
    			r++;
    		}
    	}
        return r;
    }
    
    

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {3,2,2,3};
	
		int a = removeElement(nums,3);
		System.out.println(a);
		for(int i : nums){
			System.out.println(nums[i]);
		}

	}

}
