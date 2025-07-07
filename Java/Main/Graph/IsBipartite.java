package Graph;

import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class IsBipartite {
    public static boolean isBipartite(int[][] graph) {

        int[] color = new int[graph.length];
        Arrays.fill(color, -1);

        for (int start = 0; start < graph.length; start++) {
            if  (color[start] == -1) {
                Queue<Integer> queue = new LinkedList<>();
                color[start] = 0;
                queue.add(start);

                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    for (int edge : graph[node]) {
                        if (color[edge] == -1) {
                            if (color[node] == 0) color[edge] = 1;
                            else color[edge] = 0;

                            queue.add(edge);
                        } else {
                            if (color[node] == color[edge]) return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));



        writer.close();
        reader.close();
    }
}
