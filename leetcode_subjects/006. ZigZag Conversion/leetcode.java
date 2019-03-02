
class Solution {

    public String convert(String s, int numRows) {
        if (s == null || s.length() == 0 || numRows < 1) {
            return "";
        } else if (numRows == 1) {
            return s;
        }

        StringBuilder ans = new StringBuilder(s.length());
        int interval = 2 * (numRows - 1);
        for (int i = 0; i < numRows; i++) {
            int interval1 = 2 * (numRows - i - 1);
            int interval2 = interval - interval1;

            int n = i;
            int temp = 0;
            while (n < s.length()) {
                ans.append(s.charAt(n));
                if ((temp++ % 2 == 0 || interval2 == 0) && interval1 != 0) {
                    n += interval1;
                } else {
                    n += interval2;
                }
            }
        }
        return ans.toString();
    }


}