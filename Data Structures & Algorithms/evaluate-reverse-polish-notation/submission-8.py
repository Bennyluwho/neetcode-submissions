class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack, token)
            if token == "+":
                x, y = stack.pop(), stack.pop()
                stack.append(y + x)
                continue
            if token == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
                continue
            if token == "*":
                x, y = stack.pop(), stack.pop()
                stack.append(y * x)
                continue
            if token == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
                continue
            stack.append(int(token))
        return int(stack[-1])