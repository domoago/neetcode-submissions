class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        ROWS = len(text1) + 1
        COLS = len(text2) + 1
        curr = [0] * COLS
        for i in reversed(range(ROWS - 1)):
            prev = 0
            for j in reversed(range(COLS - 1)):
                temp = curr[j]
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev
                else:
                    curr[j] = max(curr[j], curr[j + 1])
                prev = temp
        return curr[0]
                