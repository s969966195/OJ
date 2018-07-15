import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution {
	
	/*
	 * Approach 1: Brute Force
	 * Time complexity : O(n^3)
	 * Space complexity : O(min(n, m))O(min(n,m))
	 */
    public boolean allUnique(String s, int start, int end) {
    	Set<Character> set = new HashSet<>();
    	for (int i = start; i < end; i++) {
    		Character ch = s.charAt(i);
    		if (set.contains(ch)) return false;
    		set.add(ch);
    	}
    	return true;
    }
    
    public int lengthOfLongesSubstring2(String s) {
    	int n = s.length();
    	int ans = 0;
    	for (int i = 0; i < n; i++) {
    		for (int j = i + 1; j < n; j++) {
    			if (allUnique(s, i, j)) ans = Math.max(ans, j - i);
    		}
    	}
    	return ans;
    }
    
	/*
	 * Approach 2: Sliding Window
	 * Time complexity : O(2n) = O(n)
	 * Space complexity : O(min(m, n))O(min(m,n))
	 */
    public int lengthOfLongestSubstring2(String s) {
    	int n = s.length();
    	Set<Character> set = new HashSet<>();
    	int ans = 0, i = 0, j = 0;
    	while (i < n && j < n) {
    		if (!set.contains(s.charAt(j))) {
    			set.add(s.charAt(j++));
    			ans = Math.max(ans, j - i);
    		} else {
    			set.remove(s.charAt(i++));
    		}
    	}
    	return ans;
    }
    
    /*
     * Approach 3: Sliding Window Optimized
     * Time complexity : O(n)
     */
    
    // Space complexity (HashMap) : O(min(m, n))
    public int lengthOfLongestSubstring3(String s) {
    	int n = s.length(), ans = 0;
    	HashMap<Character, Integer> map = new HashMap<>();
    	for (int j = 0, i = 0; j < n; j++) {
    		if (map.containsKey(s.charAt(j))) {
    			i = Math.max(map.get(s.charAt(j)), i);
    		}
    		ans = Math.max(ans, j - i + 1);
    		map.put(s.charAt(j), j + 1);
    	}
    	return ans;
    }
    
    // Space complexity (Table): O(m)
    public int lengthOfLongesSubstring(String s) {
        int n = s.length(), ans = 0;
        int[] index = new int[128]; 
        for (int j = 0, i = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Test test = new Test();
		String s = "abcabcbb";
		System.out.println(test.lengthOfLongesSubstring(s));
	}

}
