class Solution {
public:
    int maxDepth(string s) {
        int cur = 0, max = 0;
        for(auto c: s){
            if(c == '('){
                cur++;
                if(cur > max){
                    max = cur;
                }
            }
            else if(c == ')'){
                cur--;
            }
        }
        return max;
    }
};