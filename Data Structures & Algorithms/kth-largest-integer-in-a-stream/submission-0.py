import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        temp = self.nums.copy()
        heapq.heappush(temp, -val)
        heapq.heappush(self.nums, -val)

        for i in range(self.k - 1):
            heapq.heappop(temp)
        
        return -heapq.heappop(temp)
