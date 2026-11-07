def concatenate(s1: str, s2: str) -> str:
    combinedStr = s1 + s2
    if len(combinedStr) > 10:
        return "Too long!"
    else:
        return combinedStr




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
