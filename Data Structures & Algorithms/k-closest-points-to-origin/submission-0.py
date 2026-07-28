import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [(x*x + y*y, [x,y]) for x, y in points]
        heapq.heapify(points)
        #print(points)

        out = []
        for i in range(k):
            out.append(heapq.heappop(points)[1])
        
        return out