// See https://aka.ms/new-console-template for more information
int[] nums = {0,0,0,1,0,1,1,0};
int k = 3;
int res = new Solution().MinKBitFlips(nums, k);
Console.WriteLine(res);


public class Solution {
    public int MinKBitFlips(int[] nums, int k) {
        int res = 0;
        int length = nums.Length;
        bool[] flip = new bool[length];
        int flipped = 0;

        for (int i = 0; i < length; i++) {
            if (i >= k) {
                if (flip[i - k]) {
                    flipped -= 1;
                }
            }
            if (flipped % 2 == nums[i]) {
                if (i + k > length) {
                    return -1;
                }
                flip[i] = true;
                flipped += 1;
                res += 1;
            }
        }

        return res;
    }
}
