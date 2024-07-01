int[] arr = [2,6,4,1];
bool res = new Solution().ThreeConsecutiveOdds(arr);
Console.WriteLine(res);


public class Solution {
    public bool ThreeConsecutiveOdds(int[] arr) {
        int count = 0;
        foreach (int x in arr) {
            if (x % 2 == 0) {
                count = 0;
            } else {
                count += 1;
                if (count == 3) {
                    return true;
                }
            }
        }
        return false;
    }
}
