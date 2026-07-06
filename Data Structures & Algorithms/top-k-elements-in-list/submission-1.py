import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        h = []
        for n, count in freq.items():
            heapq.heappush(h, (-count, n))
        
        out = []

        while h and len(out) < k:
            out.append(heapq.heappop(h)[1])
        
        return out