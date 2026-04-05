class MedianFinder:
    # main thing: we can't afford to sort at every insertion

    def __init__(self):
        # first half of array 
        self.max_heap = [] 
        # second half of array
        self.min_heap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            move = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -move)

        if len(self.max_heap) - len(self.min_heap) > 1:
            move = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -move)

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        