class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        res = float('-inf')
        l = 0

        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            res = max(res, prices[r] - prices[l])
        
        return res if res != float('-inf') else 0