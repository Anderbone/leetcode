package leetcode;
/*
 * #String
 * Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
			 if("".equals(s)) return "";
			 if("".equals(res)) {
				 res = s;
				 continue;
			 }
			 this is the most important part, think of it.

 */
public class _14_LongestCommonPrefix {
	
	 public static String longestCommonPrefix(String[] strs) {
		 String res = "";
		
		 for(String s : strs) { 
			 if("".equals(s)) return "";
			 if("".equals(res)) {
				 res = s;
				 continue;
			 }
			 
			 while(s.indexOf(res)!=0) {
				  if(res.length()<=1){
	                     return "";
	                 }
					else {
						res = res.substring(0, res.length()-1);
						
					}
			 }
 
		 }
		 return res;
	 }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] strs = {"aaa","aa","aaa"};
		System.out.println(longestCommonPrefix(strs));

	}

}
