class TimeMap:

    def __init__(self):
        self.ht = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ht:
            self.ht[key] = ([timestamp], [value])
            return
        
        self.ht[key][0].append(timestamp)
        self.ht[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ht:
            return ""
        
        times, values = self.ht[key] 
        l, r = 0, len(times)-1

        res = ""
        while l < r:
            m = l + (r-l)//2

            if times[m+1] > timestamp:
                r = m
            else:
                l = m + 1
        
        if times[l] <= timestamp:
            res = values[l]

        return res
            