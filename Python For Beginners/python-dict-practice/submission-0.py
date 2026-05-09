from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    pass
    mp = {}
    for i in range(len(word)):
        if word[i] in mp:
            mp[word[i]] += 1
        else:
            mp[word[i]] = 1
    return mp



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
