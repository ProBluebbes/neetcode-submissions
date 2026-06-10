class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        prefix = [0] * n # how far forward
        postfix = [0] * n # how far backward
        stack = []

        # prefix
        for i in range(n):
            while stack:
                height, index = stack[-1]
                
                if heights[i] >= height:
                    break

                prefix[index] = i-index-1 # exclusive
                stack.pop()
            
            stack.append((heights[i], i))

        while stack:
            height, index = stack.pop()
            prefix[index] = n-index-1

        # postfix
        for i in range(n-1, -1, -1):
            while stack:
                height, index = stack[-1]
                
                if heights[i] >= height:
                    break

                postfix[index] = index-i-1 # exclusive
                stack.pop()
            
            stack.append((heights[i], i))
            
        while stack:
            height, index = stack.pop()
            postfix[index] = index

        res = 0
        for i in range(n):
            area = heights[i] * (1 + prefix[i] + postfix[i])
            if area > res:
                res = area
        
        return res

