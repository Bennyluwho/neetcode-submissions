class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l, r = 0, 0
       res = 0
       while r < len(prices) - 1:
        r += 1
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
       return res
