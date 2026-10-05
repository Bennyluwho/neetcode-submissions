class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict(Counter(nums))
        temp = []
        for key, val in counter.items():
            temp.append([val, key])
        temp.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][1])
        return res