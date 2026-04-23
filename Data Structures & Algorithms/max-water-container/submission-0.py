class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        water = 0
        while l < r:
            curr = (r - l) * min(heights[r], heights[l])
            water = max(curr, water)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return water