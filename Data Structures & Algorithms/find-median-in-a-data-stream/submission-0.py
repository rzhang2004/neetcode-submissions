import heapq

class MedianFinder:

    def __init__(self):
        self.l = 0
        self.h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h, num)
        self.l += 1

    def findMedian(self) -> float:
        temp = self.h.copy()
        if self.l % 2 == 1:
            for i in range(self.l // 2):
                heapq.heappop(temp)
            return heapq.heappop(temp)
        
        for i in range(int(self.l / 2 - 1)):
            heapq.heappop(temp)
        a = heapq.heappop(temp)
        b = heapq.heappop(temp)
        return (a+b)/2
        