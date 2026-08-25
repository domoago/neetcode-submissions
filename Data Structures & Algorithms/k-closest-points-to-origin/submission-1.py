class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSort(points, 0, len(points) - 1)[0:k]
    
    def quickSort(self, arr, start, end):
        if end - start <= 0:
            return arr
        pivot = arr[end]
        leftPtr = start
        for i in range(start, end):
            if self.calculateDistance(arr[i]) < self.calculateDistance(pivot):
                temp = arr[i]
                arr[i] = arr[leftPtr]
                arr[leftPtr] = temp
                leftPtr += 1
        arr[end] = arr[leftPtr]
        arr[leftPtr] = pivot
        self.quickSort(arr, start, leftPtr - 1)
        self.quickSort(arr, leftPtr + 1, end)
        return arr

    def calculateDistance(self, point):
        return math.sqrt(pow(point[0], 2) + pow(point[1], 2))