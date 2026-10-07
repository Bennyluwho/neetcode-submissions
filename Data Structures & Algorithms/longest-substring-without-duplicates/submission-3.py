class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1
            seen.add(s[r])
            longestSub = max(longestSub, r - l + 1)
        return longestSub
