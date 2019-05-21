package leetcode;

import day15.ConvertString;

/*4631  
 * #String
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
 */
public class _6_ZigZag {
	
    public String convert(String s, int numRows) {
        int factor = numRows * 2 - 2;
        int x,y;
        if(s.length() <= numRows || numRows < 2)
            return s;
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<numRows;i++){
            if(i==0 || i==numRows-1){
                x = factor;
                y = factor;
            } else{
                x = factor - 2 * i;
                y = factor - x;
            }
             int j = i;
            boolean flag = true;
            while(j<s.length()){
                char ch = s.charAt(j);
                sb.append(ch);
                if(flag)
                    j += x;
                else
                    j += y;
                flag = !flag;
            }
        }
        return sb.toString();
    }
    
    private String convert2(String s, int numRows) {
    	if(numRows==1||s.length()<numRows|| s == null)  return s;
    	
    	StringBuilder[] sb = new StringBuilder[numRows];
    	for(int i = 0;i<numRows;i++) sb[i] = new StringBuilder();
    	int t = 2*numRows -2;
    	char[] ss = s.toCharArray();
    	for(int i = 0; i<s.length(); i++){
    		if ((i%t) < numRows) 	sb[i % t].append(ss[i]);
    		else sb[t-i%t].append(ss[i]);

    	}
    	StringBuilder ans = new StringBuilder();
    	for(int j = 0;j<sb.length;j++) {
    		ans.append(sb[j]);
    	}
    	return ans.toString();
	}
        
    public String convert3(String s, int numRows) {
        if(s == null || s.length() <= 1 || numRows == 1) return s;
        StringBuilder[] sb = new StringBuilder[numRows];
        for(int i = 0;i<numRows;i++) sb[i] = new StringBuilder();
        int i = 0, range = 2*numRows-2;
        while(i<s.length()){
            if((i%range) < numRows) sb[i % range].append(s.charAt(i));//traverse down
            else sb[ range - i % range].append(s.charAt(i));// traverse up
            i++;
        }
        StringBuilder ans = new StringBuilder();
        for(int j = 0;j< sb.length;j++) ans.append(sb[j]);
        return ans.toString();
    }
    
    
    public static void main(String[] args) {
    	
    	_6_ZigZag m = new _6_ZigZag();
//    	String ans = m.convert("PAYPALISHIRING", 3);
//    	System.out.println(ans);
    	
    	String ans2 = m.convert2("PAYPALISHIRING", 3);
    	System.out.println(ans2);
    	
		
	}

}
