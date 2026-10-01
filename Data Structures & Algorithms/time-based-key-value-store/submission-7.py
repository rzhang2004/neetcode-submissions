from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        most_recent = -float('inf')
        l = 0
        r = len(self.times[key]) - 1
        while l <= r:
            mid = (l+r)//2
            if self.times[key][mid] <= timestamp:
                most_recent = max(most_recent, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        if most_recent == -float('inf'):
            return ""
        
        return self.vals[key][most_recent]

