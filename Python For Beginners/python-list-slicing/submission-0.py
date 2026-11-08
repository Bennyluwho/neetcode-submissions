from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    new_list = []
    for i in range(1, 4):
        new_list.append(my_list[len(my_list) - i])
    return new_list[::-1]


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
