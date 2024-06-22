// See https://aka.ms/new-console-template for more information
int[] nums = {1,1,2,1,1};
int k = 3;
int res = new Solution().NumberOfSubarrays(nums, k);
Console.WriteLine(res);


public class Solution {
    public int NumberOfSubarrays(int[] nums, int k) {
        int res = 0;
        int initial_gap = 0;
        int start = 0;
        int qsize = 0;

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] % 2 == 1) {
                qsize += 1;
            }
            if (qsize == k) {
                initial_gap = 0;
                while (qsize == k) {
                    qsize -= nums[start] % 2;
                    initial_gap += 1;
                    start += 1;
                }
            }
            res += initial_gap;
        }
        return res;
    }
}
