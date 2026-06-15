class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if % 2 == 1, grab middle array and get middle num
        # if % 2 == 0, grab left of 2 middle arrays use last element

        rows = len(matrix)
        columns = len(matrix[0]) if matrix else 0

        l = 0
        r = rows * columns - 1

        while l <= r:
            m = l + (r-l)//2
            row = m // columns
            col = m % columns

            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        return False
            

