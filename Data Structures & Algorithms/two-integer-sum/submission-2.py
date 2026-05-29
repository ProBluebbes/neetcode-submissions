class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            leftover = target - nums[i]
            
            if leftover in d:
                return [d[leftover], i]

            d[nums[i]] = i