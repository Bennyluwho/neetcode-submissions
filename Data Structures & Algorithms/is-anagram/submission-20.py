class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = {}
        t_counter = {}

        for char in s:
            if char not in s_counter:
                s_counter[char] = 1
            else:
                s_counter[char] += 1
        for char in t:
            if char not in t_counter:
                t_counter[char] = 1
            else:
                t_counter[char] += 1
        print(s_counter)
        print(t_counter)

        for key, value in s_counter.items():
            if key not in t_counter:
                return False
            if key in t_counter and t_counter[key] != value:
                return False
        return True