from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dic = {}
    for i in range(0, len(word)):
        if word[i] in dic:
            dic[word[i]] += 1
        else:
            dic[word[i]] = 1
    return dic




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
