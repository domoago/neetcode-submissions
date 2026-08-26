class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for letter in s:
            if letter in mp:
                mp[letter] += 1
            else:
                mp[letter] = 1
        for letter in t:
            if letter in mp:
                mp[letter] -= 1
            else:
                return False
        for key in mp:
            if mp[key] != 0:
                return False
        return True


