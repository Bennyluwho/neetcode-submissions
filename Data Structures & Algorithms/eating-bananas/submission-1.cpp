class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int L = 1, R = *max_element(piles.begin(), piles.end());
        int res = R;
        while(L <= R) {
            int k = L + (R - L) / 2;
            int sum = 0;
            for (int i = 0; i < piles.size(); ++i) {
                sum += ceil(double(piles[i])/k);
            }
            if (sum <= h) {
                R = k - 1;
                res = k;
            } else {
                L = k + 1;
            }
        }
        return res;
    }
};
