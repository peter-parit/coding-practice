package DynamicProgrammingAndBacktracking;

import java.util.Arrays;

public class HouseRobber {
    public int rob(int[] nums) {
        int n =  nums.length;
        if (n == 0) return 0;
        if (n == 1) return 1;

        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            // Choosing the max between the sum of current and the
            // (i - 1)-th house, and the house before
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        // returns the final maximum
        return dp[n - 1];
    }

    public static void main(String[] args) {
        HouseRobber rb = new HouseRobber();
        System.out.println(rb.rob(new int[]{1,2,3,1}));
    }
}
