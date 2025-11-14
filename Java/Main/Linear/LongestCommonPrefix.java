package Linear;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ans = new StringBuilder();
        String start = strs[0];
        boolean same;
        for (int i = 0; i < start.length(); i++) {
            same = true;
            for (String str : strs) {
                if (str.length() <= i) return ans.toString();

                boolean common = str.charAt(i) == start.charAt(i);
                if (!common) {
                    same = false;
                    break;
                }
            }

            if (same) {
                ans.append(start.charAt(i));
            } else {
                return ans.toString();
            }
        }
        return ans.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String[] strs = reader.readLine().split(" ");
        LongestCommonPrefix lcp = new LongestCommonPrefix();
        System.out.println(lcp.longestCommonPrefix(strs));
    }
}
