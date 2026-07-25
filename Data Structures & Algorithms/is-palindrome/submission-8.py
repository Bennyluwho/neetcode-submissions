class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == " " or not s[l].isalnum():
                l += 1
                continue
            if s[r] == " " or not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            r -= 1
            l += 1

        return True