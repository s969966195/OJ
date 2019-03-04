
class Solution {


    public int myAtoi(String str) {
        if (str == null) {
            return 0;
        }
        String noSpaceStr = str.trim();
        if (noSpaceStr.length() == 0) {
            return 0;
        }
        StringBuilder ans = new StringBuilder();
        boolean isPositive;
        int i;
        char firstCh = noSpaceStr.charAt(0);
        if (firstCh == '-') {
            isPositive = false;
            i = 1;
        } else if (firstCh == '+') {
            isPositive = true;
            i = 1;
        } else if (isNumber(firstCh)) {
            isPositive = true;
            i = 0;
        } else {
            return 0;
        }
        if (i == 1 && noSpaceStr.length() == 1) {
            return 0;
        }
        for (int j = i; j < noSpaceStr.length(); j++) {
            char ch = noSpaceStr.charAt(j);
            if (isNumber(ch)) {
                ans.append(ch);
            } else {
                break;
            }
        }
        if (ans.length() == 0) {
            return 0;
        }
        Double res = Double.valueOf(ans.toString());
        if (!isPositive) {
            res = 0 - res;
            if (res < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        } else {
            if (res > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
        }
        return res.intValue();
    }

    private boolean isNumber(char ch) {
        if ('0' <= ch && ch <= '9') {
            return true;
        }
        return false;
    }


}