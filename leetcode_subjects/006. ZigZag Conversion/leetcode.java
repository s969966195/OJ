import java.util.ArrayList;
import java.util.List;

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

    public String convertSortByRow(String s, int numRows) {
        if (numRows == 1) return s;

        List<StringBuilder> rows = new ArrayList<>();

        for (int i = 0; i < Math.min(numRows, s.length()); i++) {
            rows.add(new StringBuilder());
        }

        int curRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1 : -1;
        }

        StringBuilder ret = new StringBuilder();
        for (StringBuilder row : rows) {
            ret.append(row);
        }
        return ret.toString();
    }


}