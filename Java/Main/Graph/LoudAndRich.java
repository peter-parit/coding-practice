package Graph;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/***
 Topological Sorting
 */
public class LoudAndRich {
    public static int[] loudAndRich(int[][] richer, int[] quiet) {
        int[] output =  new int[quiet.length];
        Arrays.fill(output, -1);

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < quiet.length; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : richer) {
            graph.get(edge[1]).add(edge[0]);
        }

        for (int person = 0; person < quiet.length; person++) {
            if (output[person] == -1) {
                dfs(graph, person, quiet, output);
            }
        }
        return output;
    }

    private static void dfs(List<List<Integer>> graph, int person, int[] quiet, int[] output) {
        int quietest = person;
        for (int neighbour: graph.get(person)) {
            if (output[neighbour] == -1)
                dfs(graph, neighbour, quiet, output);

            if (quiet[output[neighbour]] < quiet[quietest])
                quietest = output[neighbour];
        }
        output[person] = quietest;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(reader.readLine().trim());
        int[][] richer = new int[n][n];
        for (int i = 0; i < n; i++) {
            int[] entry =  Arrays.stream(reader.readLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
            richer[i] = entry;
        }
        int[] quiet = Arrays.stream(reader.readLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] res = LoudAndRich.loudAndRich(richer, quiet);
        writer.write(Arrays.toString(res));
        writer.close();
        reader.close();
    }
}
