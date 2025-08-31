package PrefixSum;

import java.io.*;
import java.util.Arrays;

class ProductArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];

        // prefix
        answer[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // suffix (right to left)
        int suffix = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *=  nums[i];
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        ProductArrayExceptSelf pa = new ProductArrayExceptSelf();

        int[] in = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] answer = pa.productExceptSelf(in);
        System.out.println(Arrays.toString(answer));

        writer.close();
    }
}