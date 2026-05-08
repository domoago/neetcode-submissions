from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    pass
    return_list = []
    for i in my_list[-3::1]:
        return_list.append(i)
    return return_list

# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
