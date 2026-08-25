class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            currMin = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / currMin)
            if hours <= h:
                high = currMin - 1
                res = min(currMin, res)
            else:
                low = currMin + 1
        return res