class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-(x**2 + y**2), x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            k -= 1
        return res