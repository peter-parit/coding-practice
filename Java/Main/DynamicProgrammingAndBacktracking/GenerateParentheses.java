package DynamicProgrammingAndBacktracking;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GenerateParentheses {
    final List<String> combinations = new ArrayList<>();
    Map<Integer, List<String>> memo = new HashMap<>();

    private void backtrack(int n, int openers, int closers, String current) {
        if (openers == 0) {
            StringBuilder currentBuilder = new StringBuilder(current);
            while (currentBuilder.length() < n * 2) {
                currentBuilder.append(")");
            }
            current = currentBuilder.toString();
            combinations.add(current);
            return;
        }

        // opened
        if (openers < n) {
            // all openers are closed
            if (closers == n - openers) {
                backtrack(n, openers - 1, closers, current + "(");
            } else {
                // not all closed
                backtrack(n, openers - 1, closers, current + "(");
                backtrack(n, openers, closers + 1, current + ")");
            }
        } else {
            // only opener possible
            backtrack(n, openers - 1, closers, current + "(");
        }
    }

    public List<String> generateParenthesis(int n) {
        backtrack(n, n, 0, "");
        return combinations;
    }

    public List<String> generateParenthesisDP(int n) {
        if (memo.containsKey(n)) return memo.get(n);

        List<String> result = new ArrayList<>();
        if (n == 0) {
            result.add("");
        } else {
            for (int i = 0; i < n; i++) {
                for (String left : generateParenthesisDP(i)) {
                    for (String right : generateParenthesisDP(n - 1 - i)) {
                        result.add("(" + left + ")" + right);
                    }
                }
            }
        }

        memo.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        GenerateParentheses gp = new GenerateParentheses();
        System.out.println(gp.generateParenthesisDP(3));
    }
}
