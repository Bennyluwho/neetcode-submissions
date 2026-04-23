class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (const auto& row : matrix) {
            if (search(row, target) != -1) return true;
        }
        return false;
    }

    int search(const vector<int>& nums, int target) {
        int L = 0, R = nums.size() - 1;

        while (L <= R) {
            int mid = (R + L) / 2;

            if (nums[mid] < target) {
                L = mid + 1;
            } else if (nums[mid] > target) {
                R = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};
