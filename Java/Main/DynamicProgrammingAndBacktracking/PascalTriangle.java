package DynamicProgrammingAndBacktracking;

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {
    public static List<List<Integer>> generate(int numRows) {

        List<List<Integer>> result = new ArrayList<>();

        for (int row = 0; row < numRows; row++) {

            List<Integer> currentRow = new ArrayList<>();
            for (int i = 0; i <= row; i++) {

                if (i == 0 || row == i) {
                    currentRow.add(1);
                } else {
                    currentRow.add(result.get(row - 1).get(i - 1)
                            + result.get(row - 1).get(i));
                }
            }
            result.add(currentRow);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(PascalTriangle.generate(5));
    }
}
