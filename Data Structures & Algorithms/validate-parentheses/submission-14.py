class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        if len(s) == 1:
            return False

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.appendleft(char)
                continue

            if len(stack) == 0:
                return False
            if char == ")" and stack.popleft() != "(":
                return False
            elif char == "}" and stack.popleft() != "{":
                return False
            elif char == "]" and stack.popleft() != "[":
                return False

        return len(stack) == 0