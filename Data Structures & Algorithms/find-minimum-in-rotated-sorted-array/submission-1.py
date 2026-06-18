class Solution:
    def findMin(self, nums: List[int]) -> int:
        return bsearch(0, len(nums)-1, nums)

def bsearch(l, r, nums):
    m = l + (r-l)//2

    if m == r:
        return nums[m]

    if nums[m] >= nums[r]:
        l = m + 1
    else:
        r = m
        
    return bsearch(l, r, nums)
