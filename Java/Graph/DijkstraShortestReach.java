public class  DijkstraShortestReach {
    // storing edges
    static class Edge {
        int dest, weight;
        Edge(int dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }

    // storing and comparing nodes for priority queue
    static class Node implements Comparable<Node> {
        int node, distance;
        Node(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }
        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }

    // main function
    public static List<Integer> shortestReach(int n, List<List<Integer>> edges, int s) {
        List<List<Edge>> graph = new ArrayList<>();
        for  (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (List<Integer> edge : edges) {
            int start = edge.get(0);
            int end = edge.get(1);
            int weight =  edge.get(2);
            graph.get(start).add(new Edge(end, weight));
            graph.get(end).add(new Edge(start, weight));
        }

        int[] distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[s] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int u = current.node;
            int currentDist =  current.distance;
            if (currentDist > distance[u]) continue;

            for (Edge edge : graph.get(u)) {
                int v = edge.dest;
                int weight = edge.weight;
                if (distance[v] > distance[u] + weight) {
                    distance[v] = distance[u] + weight;
                    pq.offer(new Node(v, distance[v]));
                }
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i == s) continue;
            res.add(distance[i] == Integer.MAX_VALUE ? -1 : distance[i]);
        }
        return res;
    }
}