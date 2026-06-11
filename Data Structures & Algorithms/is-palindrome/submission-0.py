class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        i = 0
        j = n-1

        while not i > j:
            l = s[i]
            r = s[j]

            if not l.isalnum():
                i += 1
                continue
            
            if not r.isalnum():
                j -= 1
                continue
            
            if l.lower() != r.lower():
                return False
            
            i += 1
            j -= 1

        return True


        