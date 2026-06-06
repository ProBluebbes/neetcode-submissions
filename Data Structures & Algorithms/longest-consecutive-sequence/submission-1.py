class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest = 0
        for num in nums:
            s.add(num)
        
        for num in nums:
            if num not in s:
                continue
            
            first = num
            while first - 1 in s:
                first -= 1

            curr = 0
            while first in s:
                s.remove(first)
                curr += 1
                first += 1
            
            if curr > longest:
                longest = curr

        return longest

                
            
            




