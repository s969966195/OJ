public class Solution {

    public double findMedianSortedArrays(int[] A, int[] B) {
        if (A.length > B.length) {
            int[] temp = A;
            A = B;
            B = temp;
        }
        int m = A.length;
        int n = B.length;

        int iMin = 0;
        int iMax = m;
        int halfLen = (m + n + 1) / 2;

        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            if (i < iMax && B[j-i] > A[i]) {
                iMin = iMin + 1;
            } else if (i > iMin && A[i-1] > B[j]) {
                iMax = iMax - 1;
            } else {
                int maxLeft = 0;
                if (i == 0) {
                    maxLeft = B[j-1];
                } else if (j == 0) {
                    maxLeft = A[i-1];
                } else {
                    maxLeft = Math.max(A[i-1], B[j-1]);
                }
                if ((m + n) % 2 == 1) {
                    return maxLeft;
                }
                int minRight = 0;
                if (i == m) {
                    minRight = B[j];
                } else if (j == n) {
                    minRight = A[i];
                } else {
                    minRight = Math.min(B[j], A[i]);
                }
                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
    }

}
