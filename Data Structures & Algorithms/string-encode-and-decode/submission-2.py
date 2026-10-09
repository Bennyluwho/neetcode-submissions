class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            wordLen = len(word)
            res += str(wordLen) + ","
        res += "#"
        for word in strs:
            res += word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        sizes = []
        res = []
        while s[r] != "#":
            if s[r] == ",":
                sizes.append(int(s[l:r]))
                l = r + 1
            r += 1
        
        r += 1
        l += 1
        
        for size in sizes:
            print(s[l:r+size])
            res.append(s[l:r+size])
            l += size
            r += size
        print(res)
        


        return res
