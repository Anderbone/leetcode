package leetcode;
/*#array #divide and conquer
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

来自 <https://leetcode.com/problems/maximum-subarray/description/> 
 */
public class _53_MaxSubarray {
    public static int maxSubArray(int[] nums) {
    	int max = nums[0];
    	int end = nums[0];
    	for(int i =1; i<nums.length; i++){
    	end = Math.max(nums[i], end+nums[i]);
    	max = Math.max(end, max);
    	}
    	return max;
    }
    
    public static void main(String[] args) {
		int[] a = {-2,1,-3,4,-1,2,1,-5,4};
		System.out.println(maxSubArray(a));
	}

}
