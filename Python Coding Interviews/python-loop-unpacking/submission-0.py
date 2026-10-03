from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_score = 0
    res = None
    for score in scores:
        student ,val = score
        if best_score < val:
            best_score = val
            res = student
    return res

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
