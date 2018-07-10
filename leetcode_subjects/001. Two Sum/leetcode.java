import java.util.HashMap;
import java.util.Map;

public class Test {

	/*
	 * Approach 1: Brute Force
	 * Time complexity : O(n^2)
	 * Space complexity : O(1)O(1)
	 */
    public int[] twoSum1(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
        {
        	for (int j = i + 1; j < nums.length; j++)
        	{
        		if (nums[i] + nums[j] == target)
        		{
        			return new int[] { i, j };
        		}
        	}
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    /*
     * Approach 2: Two-pass Hash Table
     * Time complexity : O(n)
     * Space complexity : O(n)
     */
    public int[] twoSum(int[] nums, int target) {
    	Map<Integer, Integer> map = new HashMap<>();
    	for (int i = 0; i < nums.length; i++) {
    		map.put(nums[i], i);
    	}
    	for (int i = 0; i < nums.length; i++) {
    		int complement = target - nums[i];
    		if (map.containsKey(complement) && map.get(complement) != i) {
    			return new int [] { i, map.get(complement) };
    		}
    	}
    	throw new IllegalArgumentException("No two sum solution");
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Test test = new Test();
		for (int element : test.twoSum(new int[] {2, 7, 11, 15}, 9))
		{
			System.out.println(element);
		}
	}

}
