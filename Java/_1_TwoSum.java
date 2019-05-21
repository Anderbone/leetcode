package leetcode;

import java.util.HashMap;
/*
 * #easy #array #hash table
 * Given an array of integers, return indices of the two numbers 
 * such that they add up to a specific target.
 * You may assume that each input would have exactly one solution, 
 * and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 */

public class _1_TwoSum {
    public static int[] twoSum1(int[] nums, int target) {
		int[] ans = new int[2];
		for(int i=0; i<nums.length; i++){
			for(int j =0; j<nums.length; j++){
				while(i!=j){
					if(target - nums[i] == nums[j]){
						ans[0] = i;
						ans[1] = j;	
						return ans;
					}
				}
			}
		}
    	return ans;
 
    }
    public static int[] twoSum2(int[] nums, int target){
    	int[] ans = new int[2];
    	HashMap<Integer, Integer> ha = new HashMap<Integer,Integer>();
    	for(int i = 0; i<nums.length; i++){
    		if(ha.containsKey(target - nums[i])){
    			ans[0] = i;
    			ans[1] = ha.get(target - nums[i]);
    			return ans;
    		}else{
    			ha.put(nums[i],i);
    		}
    	}
    	return null;
    }
    public static int[] twoSum3(int[] nums, int target){
    	HashMap<Integer, Integer> map1=new HashMap<Integer, Integer>();
    	int[] arr=new int[2];

    		for(int i=0; i<nums.length; i++){
    			int ss=target-nums[i];
    			if (map1.get(ss) != null)
    				{
    				arr[0]=map1.get(ss);
    				arr[1]=i;
    				return arr;
    				}
    			else{
    				map1.put(nums[i], i);
    				}
    			}
    		
    		return null;
    		}

    
    
    
    public static void main(String[] args) {
		int[] nums = {2,7,11,15};
		int t = 9;
		int a[] = twoSum3(nums,t);
		System.out.println(a[0]);
		System.out.println(a[1]);
		
	}
}
