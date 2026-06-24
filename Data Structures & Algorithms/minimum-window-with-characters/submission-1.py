class Solution:
    def minWindow(self, s: str, t: str) -> str:
        used = {}
        for c in t:
            used[c] = used.get(c, 0) + 1

        l = 0
        curr = {}
        sl = 2000
        sr = 4000
        for i in range(len(s)):
            c = s[i]
            
            if c not in used:
                continue

            curr[c] = curr.get(c, 0) + 1

            while equalOrGreater(used, curr):
                if i - l < sr - sl:
                    sl = l
                    sr = i
                
                if s[l] in curr:
                    curr[s[l]] -= 1
                    if curr[s[l]] == 0:
                        del curr[s[l]]
                
                l += 1

        if sr - sl < 1000:
            return s[sl:sr+1]
        return ""

def equalOrGreater(this, that):
    if len(this) != len(that):
        return False

    for key, val in this.items():
        if key not in that or that[key] < val:
            return False
    return True