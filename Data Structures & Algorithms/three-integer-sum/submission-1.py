class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        i = 0
        while i < n-1:
            l = i+1
            r = n-1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while r > i:
                        r -= 1
                        if nums[r] != nums[r+1]:
                            break
                    
                    while l < n-1:
                        l += 1
                        if nums[l] != nums[l-1]:
                            break

            while i < n-1:
                i += 1
                if nums[i] != nums[i-1]:
                    break

        return res


