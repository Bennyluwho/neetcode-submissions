class Solution:
    def isPalindrome(self, s: str) -> bool:
        token = ""
        for char in s:
            if char.isalnum():
                token += char.lower()

        l, r = 0, len(token) - 1
        while l < r:
            if token[l] != token[r]:
                return False
            l += 1
            r -= 1

        return True