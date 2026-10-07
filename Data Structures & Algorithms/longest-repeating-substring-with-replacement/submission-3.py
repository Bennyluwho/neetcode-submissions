class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        # print(max(counter))
        res = 1
        if len(s) == 1:
            return 1
        
        l = 0
        for r in range(len(s)):
            if s[r] not in counter:
                counter[s[r]] = 1
            else:
                counter[s[r]] += 1
            
            max_frequency = max(counter.values())
            while (r - l + 1) - max_frequency > k:
                counter[s[l]] -= 1
                l += 1
                max_frequency = max(counter.values())
                 
            res = max(res, (r - l) + 1)
        print(res)

        return res
