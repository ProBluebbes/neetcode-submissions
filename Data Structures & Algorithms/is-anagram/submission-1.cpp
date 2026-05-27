class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        for (char c : s) {
            sMap[c]++;
        }

        for (char c : t) {
            tMap[c]++;
        }

        for (const auto& [key, value] : sMap)
            if (tMap[key] != value)
                return false;

        for (const auto& [key, value] : tMap)
            if (sMap[key] != value)
                return false;

        return true;
    }
};
