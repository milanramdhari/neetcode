class MedianFinder:
    # main thing: we can't afford to sort at every insertion

    def __init__(self):
        # self.arr = []
        self.min_heap = [] 
        

    def addNum(self, num: int) -> None:
        # self.arr.append(num)
        heapq.heappush(self.min_heap, num)
        # self.arr.sort()
        

    def findMedian(self) -> float:
        length = len(self.min_heap)
        recover = []
        res = 0
        
        # odd
        if length % 2: 
            for i in range(length//2):
                recover.append(heapq.heappop(self.min_heap))
            res = self.min_heap[0]
        else:
            for i in range(length//2 - 1):
                recover.append(heapq.heappop(self.min_heap))
            num1 = heapq.heappop(self.min_heap)
            num2 = self.min_heap[0]
            heapq.heappush(self.min_heap, num1)
            res = (num1 + num2) / 2 
        
        for num in recover:
            heapq.heappush(self.min_heap, num)

        return res
        
        