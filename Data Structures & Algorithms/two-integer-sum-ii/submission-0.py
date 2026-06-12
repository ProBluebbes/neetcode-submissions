class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index2-index1 must be less than target
        n = len(numbers)
        l = 0
        r = n-1

        while True:
            res = numbers[l]+numbers[r]
            if res == target:
                return [l+1, r+1]
            if res > target:
                r -= 1
            if res < target:
                l += 1