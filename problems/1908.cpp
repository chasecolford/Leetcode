class Solution {
public:
    bool nimGame(vector<int>& piles) {
        return accumulate(begin(piles), end(piles), 0, bit_xor<int>());
    }
};

// see: https://cp-algorithms.com/game_theory/sprague-grundy-nim.html