class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for string in strs:
            chars = {}
            for char in string:
                chars[char] = chars.get(char, 0) + 1;

            imm = tuple(sorted(chars.items()))
            grouped[imm] = grouped.get(imm, []) + [string]

        sol = []
        for val in grouped.values():
            sol += [val]

        return sol