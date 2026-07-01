class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]:
                x = nums[i]
                if not nums[x-1]:
                    return x
                nums[i] = nums[x-1]
                nums[x-1] = None

        
        
        #1 2 3 4 5
        #None 2 3 4 5
        # 5 4 3 2 1
        # 1 4 3 2 None




        