int[] nums = {3};
int n = 8;

Console.WriteLine($"{new Solution().MinPatches(nums, n)}");


public class Solution {
    public int MinPatches(int[] nums, int n) {
        int miss = 1;
        int result = 0;
        int i = 0;

        while (miss <= n) {
            if (i < nums.Length && nums[i] <= miss) {
                miss += nums[i];
                i += 1;
            } else {
                Console.WriteLine($"{miss}");
                miss += miss;
                result += 1;
            }
        }

        return result;
    }
}
