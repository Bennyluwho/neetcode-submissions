class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            else:
                biggest = arr[i + 1]
            for j in range(i + 1, len(arr)):
                biggest = max(arr[j], biggest)
            arr[i] = biggest
        