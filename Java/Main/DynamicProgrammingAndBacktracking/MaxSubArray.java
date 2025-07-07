package DynamicProgrammingAndBacktracking;

import java.io.*;
import java.util.Arrays;

public class MaxSubArray {
    public static int maxSubArray(int[] nums) {
        int res = nums[0];
        int maxEnding = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // choose between continuing or starting anew (which one results to more)
            maxEnding = Math.max(nums[i], maxEnding + nums[i]);

            // update result
            res = Math.max(maxEnding, res);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        writer.write("Max subarray: " + MaxSubArray.maxSubArray(arr));
        writer.newLine();

        writer.close();
        reader.close();
    }
}
