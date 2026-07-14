class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res = 100000;
        int curSum = 0;

        int l = 0;

        for (int r = 0; r < nums.length; r++) {
            curSum += nums[r];
            while (curSum >= target) {
                res = Math.min(res, (r - l) + 1);
                curSum -= nums[l];
                l++;
            }
            System.out.println(curSum);
        }

        System.out.println(res);


        if (res == 100000) return 0;
        return res;
    }
}