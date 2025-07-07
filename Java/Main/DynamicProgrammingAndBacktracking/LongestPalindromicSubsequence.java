package DynamicProgrammingAndBacktracking;

public class LongestPalindromicSubsequence {
    public static int longestPalindromicSubsequence(String s, int k) {
        int originalLPS = getLPSLength(s);
        int n = s.length();
        int validInsertions = 0;

        for (int i = 0; i <= n; i++) {
            for (char ch = 'a'; ch <= 'z'; ch++) {
                String modified = s.substring(0, i) + ch + s.substring(i);
                int newLPS = getLPSLength(modified);
                if (newLPS >= originalLPS + k) {
                    validInsertions++;
                }
            }
        }

        return validInsertions;
    }

    private static int getLPSLength(String s) {
        int n = s.length();
        if (n == 0) return 0;

        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;

                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = 2 + ((i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0);
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[0][n - 1];
    }
}