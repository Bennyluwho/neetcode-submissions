class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedText = ''.join(sorted(strs[1]))
        # print(sortedText)
        words = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in words:
                words[sortedWord].append(word)
            else:
                words[sortedWord] = []
                words[sortedWord].append(word)
        return list(words.values())