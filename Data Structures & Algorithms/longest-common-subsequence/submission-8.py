class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1) + 1
        COLS = len(text2) + 1
        curr = [0] * COLS
        for i in reversed(range(ROWS - 1)):
            prev = curr.copy()
            for j in reversed(range(COLS - 1)):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
        return curr[0]