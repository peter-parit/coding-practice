package Graph;

import java.util.ArrayList;
import java.util.List;

public class CutTheTree {

    // main function
    public static int cutTheTree(List<Integer> data, List<List<Integer>> edges) {
        int n = data.size();
        List<List<Integer>> tree = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            tree.add(new ArrayList<>());
        }

        // make tree
        for (List<Integer> edge : edges) {
            int u = edge.get(0);
            int v = edge.get(1);
            tree.get(u).add(v);
            tree.get(v).add(u);
        }

        int totalSum = data.stream().mapToInt(Integer::intValue).sum();
        int[] minDiff = {Integer.MAX_VALUE};
        boolean[] visited = new boolean[n + 1];

        dfsMinDiff(1, data, tree, visited, totalSum, minDiff);

        return minDiff[0];
    }

    // dfs traversal
    private static int dfsMinDiff(int node, List<Integer> data, List<List<Integer>> tree,
                                  boolean[] visited, int totalSum, int[] minDiff) {
        visited[node] = true;
        int subtreeSum = data.get(node - 1);

        // dfs traversal + adding node weights
        for (int neighbor : tree.get(node)) {
            if (!visited[neighbor]) {
                subtreeSum += dfsMinDiff(neighbor, data, tree, visited, totalSum, minDiff);
            }
        }

        // find other subtree
        int otherTreeSum = totalSum - subtreeSum;
        int diff = Math.abs(otherTreeSum - subtreeSum);

        // if lower abs diff
        if (diff < minDiff[0]) {
            minDiff[0] = diff;
        }

        return subtreeSum;
    }
}