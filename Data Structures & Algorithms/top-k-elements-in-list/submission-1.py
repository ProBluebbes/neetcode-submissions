class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        buckets = [[] for i in range(n + 1)]
        for key, val in d.items():
            buckets[val] += [key]

        res = []
        for i in reversed(range(n + 1)):
            if len(buckets[i]):
                for val in buckets[i]:
                    res += [val]
                    if len(res) >= k:
                        return res
