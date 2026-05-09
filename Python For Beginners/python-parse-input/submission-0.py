from typing import List

def read_integers() -> List[int]:
    pass
    nums = []
    for num in input().split(","):
        nums.append(int(num))
    return nums
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
