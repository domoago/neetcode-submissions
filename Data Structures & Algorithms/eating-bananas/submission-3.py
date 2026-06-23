class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            k = (left + right) // 2
            timeElapsed = 0
            for pile in piles:
                timeElapsed += math.ceil(float(pile) / k)
            if timeElapsed <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result