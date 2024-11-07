class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""

        return self.binary_search(self.store[key], timestamp)
    
    def binary_search(self, arr, timestamp):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if arr[r][1] < timestamp:
            return arr[r][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)