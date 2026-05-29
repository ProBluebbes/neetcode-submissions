class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            val = nums[i]
            if (val in d):
                return True
            d[val] = True

        return False