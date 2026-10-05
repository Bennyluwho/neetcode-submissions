class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter1 = {}
        counter2 = {}

        for char in s:
            if char not in counter1:
                counter1[char] = 1
            else:
                counter1[char] += 1
        
        for char in t:
            if char not in counter2:
                counter2[char] = 1
            else:
                counter2[char] += 1
        
        return counter1 == counter2