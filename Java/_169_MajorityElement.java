package leetcode;

import java.util.Arrays;

/*
 * #169 第一个独立完成的leetcode
 * #array #divide and conquer #bit manipulation
 */
public class _169_MajorityElement {
	
	static int majority(int[] nums){
		if(nums.length == 1){
			return nums[0];
		}
		int line = (int) Math.ceil(nums.length/2.0);
		Arrays.sort(nums);
		for(int i = 0; i<nums.length; i++){
			if(nums[i] == nums[i+line-1]){
				return nums[i];
			}
		}
		return -1;
	}
	
	public static void main(String[] args) {
		int[] a = {3,2,3};
		int ans = majority(a);
		System.out.println(ans);
	}

}
