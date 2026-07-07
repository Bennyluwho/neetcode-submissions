class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        res = -1

        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for key, val in hashmap.items():
            if key == val:
                res = max(res, key)
        
        return res
