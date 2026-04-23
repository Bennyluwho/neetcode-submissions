class Solution {
public:
    int recurse(int i, vector<int>& profit, vector<int>& weight, int capacity){
        if (i < 0 || capacity == 0) return 0;
       
        int take = (capacity >= weight[i]) ? profit[i] + recurse(i - 1, profit, weight, capacity - weight[i]) : 0;
        int notake = recurse(i - 1, profit, weight, capacity);

        return max(take,notake);
    }

    int maximumProfit(vector<int>& profit, vector<int>& weight, int capacity) {
        return recurse(profit.size() - 1, profit, weight, capacity);
    }
};
