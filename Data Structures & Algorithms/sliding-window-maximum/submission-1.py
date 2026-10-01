import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        n = [-x for x in nums]
        h = [(n[i], i) for i in range(k)]
        heapq.heapify(h)
        res = []

        while l + k - 1 < len(nums):
            heapq.heappush(h, (n[l+k-1], l+k-1))
            while h[0][1] < l:
                heapq.heappop(h)
            res.append(-h[0][0])
            if n[l] == h[0]:
                heapq.heappop(h)
            l += 1
        
        return res