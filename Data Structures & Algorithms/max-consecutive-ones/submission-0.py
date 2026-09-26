class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, counter)
                counter = 0
                continue
            counter += 1
        
        res = max(res, counter)
        
        return res