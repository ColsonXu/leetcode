class TimeMap:

    slots = ["map"]

    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        stack = self.map.get(key, [])
        l = 0
        r = len(stack) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if stack[mid][0] <= timestamp:
                res = stack[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
