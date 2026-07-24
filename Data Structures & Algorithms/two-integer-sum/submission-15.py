class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in seen:
                seen[nums[i]] = i
            else:
                return [seen[temp], i]

        return [0,0]