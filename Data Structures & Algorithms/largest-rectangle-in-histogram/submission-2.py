class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, hei = stack.pop()
                res = max(res, hei*(i-ind))
                start = ind

            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            res = max(res, h*(n-i))

        return res

