class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        i = n//2
        while l <= r:
            if nums[i] > target:
                r = i-1
            elif nums[i] < target:
                l = i+1
            else:
                return i
            
            i = (r+l)//2
        return -1