class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int l = 0;
        int r = 0;

        while (r < prices.length) {
            if (prices[r] < prices[l]) {
                l = r;
            }
            maxProfit = Math.max(prices[r] - prices[l], maxProfit);
            r++;
        }
        return maxProfit;
    }
}
