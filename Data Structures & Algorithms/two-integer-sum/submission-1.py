class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            leftover = target - nums[i]
            
            if leftover in d:
                if (d[leftover] == i):
                    continue
                return [i, d[leftover]]
            