package leetcode;
/*
 * #array #backtracking #bit manipulation

 * Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

 */
import java.util.ArrayList;
import java.util.List;

public class _78_Subsets {
	
	static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for(int n : nums){
            int size = result.size();
            for(int i=0; i<size; i++){
                List<Integer> subset = new ArrayList<>(result.get(i));
                subset.add(n);
                
                result.add(subset);
            }
        }
        return result;
    }
	
	static List<List<Integer>> subsets2(int[] nums) {
		List<List<Integer>> res = new ArrayList<>();
		res.add(new ArrayList<>());
		for(int n : nums) {
			int size = res.size();
			for(int i = 0; i<size; i++) {
				List<Integer> subset = new ArrayList<>(res.get(i));
				subset.add(n);
				res.add(subset);
				
			}
		}
		return res;
	}
	
	
	public static void main(String[] args) {
		int[] a = {1,2,3};
		List<List<Integer>> ans = subsets2(a);
		for(List<Integer> l: ans){
			System.out.println();
			for(Integer i:l){
				System.out.print(i);
				
			}
		}
	
	}

}
