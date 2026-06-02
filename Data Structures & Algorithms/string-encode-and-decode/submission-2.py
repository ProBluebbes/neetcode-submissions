class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string))
            s += "#"
            s += string

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        pos = 0
        strLen = ""

        if (len(s) == 0):
            return strs

        while pos != -1:
            if (s[pos] == "#"):
                if pos >= len(s) - 1:
                    strs.append("")
                    return strs
                start = pos + 1
                end = start + int(strLen)
                strs.append(s[start:end])
                strLen = ""
                if (end >= len(s)-1):
                    pos = -1
                else:
                    pos = end
                continue
            strLen += s[pos]
            pos += 1


        return strs

