class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        res = 0

        while r > l:
            area = (r-l)*min(heights[l], heights[r])
            if area > res:
                res = area

            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
