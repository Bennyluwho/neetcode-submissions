class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int compliment = target - nums[i];

            System.out.println(compliment);

            if (seen.containsKey(compliment)) {
                return new int[] {seen.get(compliment), i};
            } else {
                seen.put(nums[i], i);
            }
        }
        return null;
    }
}
