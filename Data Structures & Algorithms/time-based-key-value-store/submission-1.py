class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
            self.db[key].append((value, timestamp))
        else:
            self.db[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""

        values = self.db[key]
        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2
            value, time = values[middle]

            if time <= timestamp:
                # This is a valid answer, but there may be
                # a later valid timestamp.
                result = value
                left = middle + 1
            else:
                # This timestamp is too large.
                right = middle - 1

        return result