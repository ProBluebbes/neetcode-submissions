class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s2)
        s1map = {}
        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1
        
        currMap = {}
        l = 0
        for i in range(n):
            c = s2[i]
            if c not in s1map:
                currMap = {}
                l = i + 1
                continue
            
            currMap[c] = currMap.get(c, 0) + 1
            if currMap[c] > s1map[c]:
                while True:
                    currMap[s2[l]] -= 1
                    if currMap[s2[l]] == 0:
                        del currMap[s2[l]]

                    if s2[l] == c:
                        l += 1
                        break
                    l += 1
            
            if currMap == s1map:
                return True

        return False


