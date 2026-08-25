class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.mergeSort(points, 0, len(points) - 1)[0:k]
    
    def mergeSort(self, arr, start, end):
        if end - start <= 0:
            return arr
        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)
        return arr
    
    def merge(self, arr, start, mid, end):
        leftHalf = arr[start:mid + 1]
        rightHalf = arr[mid + 1:end + 1]

        leftPtr = rightPtr = 0
        mergePtr = start
        
        while leftPtr < len(leftHalf) and rightPtr < len(rightHalf):
            if self.calculateDistance(leftHalf[leftPtr]) < self.calculateDistance(rightHalf[rightPtr]):
                arr[mergePtr] = leftHalf[leftPtr]
                mergePtr += 1
                leftPtr += 1
            else:
                arr[mergePtr] = rightHalf[rightPtr]
                mergePtr += 1
                rightPtr += 1
        while leftPtr < len(leftHalf):
            arr[mergePtr] = leftHalf[leftPtr]
            mergePtr += 1
            leftPtr += 1
        while rightPtr < len(rightHalf):
            arr[mergePtr] = rightHalf[rightPtr]
            mergePtr += 1
            rightPtr += 1
        

    def calculateDistance(self, point):
        return math.sqrt(pow(point[0], 2) + pow(point[1], 2))