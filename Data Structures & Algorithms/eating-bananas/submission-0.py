class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        cap = 0

        for i in range(n):
            cap = max(cap, piles[i])

        l = 1
        r = cap
        res = None
        m = 0

        while True:
            m = l + (r-l)//2
            hours = 0
            for i in range(n):
                hours += math.ceil(piles[i]/m)

            if l == r:
                break

            if hours > h:
                l = m + 1
            else:
                r = m
        
        return m

            
            
            