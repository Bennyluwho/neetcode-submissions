class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        stack.append(0)
        for i in range(1, len(temperatures)):
            # print(i, temperatures[stack[-1]])
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                curr = stack.pop()
                res[curr] = i - curr
            stack.append(i)          
        
        return res