class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        resRow = -1
        for i in range(len(matrix)):
            # print(matrix[i],matrix[i][-1])
            if matrix[i][-1] >= target:
                resRow = i
                break

        if resRow == -1:
            return False
            
        l, r = 0, len(matrix[resRow]) - 1
        res = matrix[resRow]
        # print(res)

        while l <= r:
            mid = l + (r - l) // 2
            # print(res[mid], mid)
            
            if res[mid] < target:
                l = mid + 1
            elif res[mid] > target:
                r = mid - 1
            else:
                return True


        return False