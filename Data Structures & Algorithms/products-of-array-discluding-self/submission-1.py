class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0
        total = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total *= num

        sol = [0] * n
        if (zeros >= 2):
            return sol

        if (zeros == 1):
            for i in range(n):
                if (nums[i] == 0):
                    sol[i] = total
            return sol
        
        for i in range(n):
            sol[i] = int(total * 1/nums[i])

        return sol