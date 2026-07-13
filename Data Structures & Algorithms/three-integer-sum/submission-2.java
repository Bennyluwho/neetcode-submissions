class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        Set<List<Integer>> res = new HashSet<>();

        for (int i = 0; i < nums.length - 1; i++) {
            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum > 0) {
                    r -= 1;
                } else if (sum < 0) {
                    l += 1;
                } else {
                    res.add(List.of(nums[i], nums[l], nums[r]));
                    r -= 1;
                    l += 1;
                }
            }
            
        }

        return new ArrayList<>(res);
    }
}
