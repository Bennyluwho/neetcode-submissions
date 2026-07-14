class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int l = 0;
        int r = k - 1;
        int res = 0;
        int sum = 0;

        while (r < arr.length) {
            System.out.println(l + " " + r);
            for(int i = l; i <= r; i++) {
                sum += arr[i];
            }
            int avg = sum / k;
            System.out.println(avg);
            if (avg >= threshold) {
                res += 1;
            }
            
            l++;
            r++;
            sum = 0;
        }
        return res;
    }
}