package DynamicProgrammingAndBacktracking;

import java.util.Arrays;

public class LongIncreasingSubsequence {
    private int LISAtIndex(int[] A, int index) {
        if (index == 0)
            return 1;

        int max = 1;
        for (int i = 0; i < index; i++) {
            if (A[i] < A[index]) {
                max = Math.max(max, LISAtIndex(A, i) + 1);
            }
        }
        return max;
    }
    public int LIS(int[] A) {

        int lis = 1;
        for (int i = 1; i < A.length; i++) {
            lis = Math.max(lis, LISAtIndex(A, i));
        }
        return lis;
    }

    public static void main(String[] args) {
        LongIncreasingSubsequence sol = new LongIncreasingSubsequence();
        System.out.println(sol.LIS(new int[]{3, 1, 8, 2, 5}));
    }
}
