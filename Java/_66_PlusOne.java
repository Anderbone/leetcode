package leetcode;
/*
 * #array #math
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

 */

public class _66_PlusOne {
    public static int[] plusOne(int[] digits) {
        int len = digits.length;
        int num = 0;
        for(int i=len-1; i>=0; i--){
        	num = (int) (num + digits[i]*Math.pow(10, len-i-1));
        }
        num = num + 1;
        String str = Integer.toString(num);
        int[] ans = new int[str.length()];
        for(int i = 0; i<ans.length; i++){
        	char c = str.charAt(i);
        	String s = String.valueOf(c);
        	int a = Integer.parseInt(s);
        	ans[i] = a;
        }
        return ans;
    }
    public static int[] plusOne2(int[] digits) {
        for (int i = digits.length - 1; i >=0; i--) {
            if (digits[i] != 9) {
                digits[i]++;
                break;
            } else {
                digits[i] = 0;
            }
        }
        if (digits[0] == 0) {
            int[] res = new int[digits.length+1];
            res[0] = 1;
            return res;
        }
        return digits;
    }
    
    public static void main(String[] args) {
    	
		int[] a= {8,7,6,5,4,3,2,1,0};
		int[] b = plusOne(a);
		for(int i: b){
			System.out.println(i);
		}
		
	}

}
