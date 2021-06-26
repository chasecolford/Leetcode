/*
* Given an array of unique integers salary where salary[i] is the salary of the employee i.
* Return the average salary of employees excluding the minimum and maximum salary.
*/
class Solution {
public:
    double average(vector<int>& salary) {
        int maxxy = INT_MIN;
        int minny = INT_MAX;
        double summy = 0;
        for(int v : salary){
            if(v > maxxy){maxxy = v;}
            if(v < minny){minny = v;}
            summy += (double) v;
        }
        return (summy - minny - maxxy) / (salary.size() - 2);
    }
};