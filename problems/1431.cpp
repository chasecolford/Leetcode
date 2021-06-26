class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = *max_element(candies.begin(), candies.end());
        vector<bool> res;
        for (int i = 0; i < candies.size(); i++)
        {
            if(candies[i] + extraCandies < max)
                res.push_back(false);
            else
                res.push_back(true);
        }
        return res;
    }
};