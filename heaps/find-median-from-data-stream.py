import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def __str__(self):
        return str(self.__dict__)
        
    def addNum(self, num: int) -> None:

        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
            return
        
        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # rebalance
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        return (self.minHeap[0] - self.maxHeap[0]) / 2

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(12)
obj.addNum(1)
obj.addNum(8)
obj.addNum(17)
obj.addNum(50)
print(obj.findMedian())
print(obj)

