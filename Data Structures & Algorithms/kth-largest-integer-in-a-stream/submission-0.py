class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        res = self.heap[-1]
        stack = []
        for i in range(self.k):
            stack.append(heapq.heappop(self.heap))
            res = stack[-1]
        while stack:
            heapq.heappush(self.heap, stack.pop())
        return -res
