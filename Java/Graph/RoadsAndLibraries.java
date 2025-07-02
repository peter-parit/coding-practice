public class RoadsAndLibraries {
    public static long roadsAndLibraries(int n, int c_lib, int c_road, List<List<Integer>> cities) {
        if (c_lib <= c_road) {
            return (long) n * c_lib;
        }

        long totalCost = 0L;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (List<Integer> city : cities) {
            adj.get(city.get(0)).add(city.get(1));
            adj.get(city.get(1)).add(city.get(0));
        }

        boolean[] visited = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                long numCities = dfs(i, adj, visited);
                totalCost += c_lib + (numCities - 1) * c_road;
            }
        }
        return totalCost;
    }

    private static long dfs(int start, List<List<Integer>> adjVertices, boolean[] isVisited) {
        Stack<Integer> stack = new Stack<>();
        stack.push(start);
        long count = 0L;
        while (!stack.isEmpty()) {
            int current = stack.pop();

            // if not visited, add to count
            if (!isVisited[current]) {
                isVisited[current] = true;
                count++;
                for (int dest : adjVertices.get(current)) {
                    if (!isVisited[dest]) {
                        stack.push(dest);
                    }
                }
            }
        }
        return count;
    }
}