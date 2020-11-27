class Solution {
public:
    std::unordered_map<char, int> m;
    int firstUniqChar(string s) {
        for (auto &c : s) {
            m[c]++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (m[s[i]] == 1) return i;
        }
        return -1;
    }   
};