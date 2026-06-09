class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        results = [0] * n
        
        last = 101
        for i in range(n):
            t = temperatures[i]
            if t <= last:
                stack.append(i)
                last = t
                continue

            while stack:
                if temperatures[stack[-1]] < t:
                    index = stack.pop()
                    results[index] = i-index
                    continue
                break

            stack.append(i)
            last = t   

        return results