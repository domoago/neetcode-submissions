def concatenate(s1: str, s2: str) -> str:
    pass
    length = len(s1 + s2)
    if length <= 10:
        return s1 + s2
    return "Too long!"




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
