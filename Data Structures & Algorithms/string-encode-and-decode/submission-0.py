class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            for char in string:
                s += char
            s += "\u0257"

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        curr = ""
        for char in s:
            if char == "\u0257":
                strs.append(curr)
                curr = ""
                continue
            curr += char

        return strs

