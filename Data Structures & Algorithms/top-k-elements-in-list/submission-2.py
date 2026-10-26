import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) - 1
        
        h = [(b,a) for a,b in counts.items()]
        heapq.heapify(h)

        out = []
        for i in range(k):
            out.append(heapq.heappop(h)[-1])
        
        return out