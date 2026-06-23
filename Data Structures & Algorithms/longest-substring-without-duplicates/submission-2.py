class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        res = 0
        deq = collections.deque()
        seen = set()

        for c in s:
            if c in seen:
                while True:
                    last = deq.popleft()
                    seen.remove(last)
                    curr -= 1
                    if last == c:
                        break
            curr += 1
            res = max(res, curr)
            seen.add(c)
            deq.append(c)

        return res
        