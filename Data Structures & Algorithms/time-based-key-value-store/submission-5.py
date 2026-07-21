class TimeMap:

    def __init__(self):
        self.values = defaultdict(dict)
        # key: {time: value}
        self.times = defaultdict(list)
        # key: sorted list of times
    def set(self, key: str, value: str, timestamp: int) -> None:
        # set value at time
        self.values[key][timestamp] = value
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # search for latest valid time
        arr = self.times[key]
        if not arr:
            return ""
        l = 0
        r = len(arr) - 1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == timestamp:
                return self.values[key][timestamp]
            elif arr[mid] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if arr[r] < timestamp:
            return self.values[key][arr[r]]
        else:
            return ""
