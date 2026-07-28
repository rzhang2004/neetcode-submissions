import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone2 < stone1:
                heapq.heappush(stones, stone2 - stone1)
        
        if not stones:
            return 0
        
        return -heapq.heappop(stones)