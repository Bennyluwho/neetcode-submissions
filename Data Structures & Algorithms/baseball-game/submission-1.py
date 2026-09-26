class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(y)
                stack.append(x)
                stack.append(x + y)
            elif op == "D":
                x = stack.pop()
                stack.append(x)
                stack.append(x * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
            print(stack)
        return sum(stack)