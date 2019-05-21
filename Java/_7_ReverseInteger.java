package leetcode;

public class _7_ReverseInteger {
	
    public static int reverse(int x) {
        long ans = 0;
        long num = (long)x;
        while(num!=0) {
        	ans *= 10;
        	ans += num % 10;
        	num /= 10;
        }
        
        int test = (int) ans;
        if(test == ans) 
        	return test;
        
        return 0;
    }

    public static int myreverse(int x) {
		// TODO Auto-generated method stub
        long ans = 0;
        int num = x;
        while(num!=0){
            ans *= 10;
            ans += num % 10;
            num /= 10;
        }
        int text = (int)ans;
        if(x!=0) return text;
        else return 0;

	}
    
    public static void main(String[] args) {
		System.out.println(reverse(123));
		System.out.println(myreverse(123));
		
	}

}
