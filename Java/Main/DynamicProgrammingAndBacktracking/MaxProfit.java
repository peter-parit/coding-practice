package DynamicProgrammingAndBacktracking;

public class MaxProfit {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0; // we return 0 if no profit is possible

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price; // lowest buy
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice); // find best sell
            }
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        int[] prices = new int[]{7, 1, 5, 3, 6, 4};
        System.out.println(new MaxProfit().maxProfit(prices));
    }
}
