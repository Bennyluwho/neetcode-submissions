class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in mapped:
                mapped[key] = []
            mapped[key].append(s)
        return list(mapped.values())