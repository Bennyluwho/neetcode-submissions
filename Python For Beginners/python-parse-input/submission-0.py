from typing import List

def read_integers() -> List[int]:
    stringList = input().split(",")
    res = []
    for i in range(0, len(stringList)):
        res.append(int(stringList[i]))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
