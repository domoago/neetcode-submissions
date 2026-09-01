class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while n > 0:
            bit = n & 1
            res = res | (bit << 31 - count)
            n = n >> 1
            count += 1
        return res