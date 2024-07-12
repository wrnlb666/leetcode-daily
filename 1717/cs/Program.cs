string s = "cdbcbbaaabab";
int x = 4;
int y = 5;
int res = new Solution().MaximumGain(s, x, y);
Console.WriteLine(res);



public class Solution {
    public int MaximumGain(string s, int x, int y) {
        char a;
        char b;
        if (x > y) {
            (a, b) = ('a', 'b');
        } else {
            (a, b) = ('b', 'a');
            (x, y) = (y, x);
        }

        int aCount = 0;
        int bCount = 0;
        int res = 0;

        foreach (char c in s) {
            if (c == a) {
                aCount += 1;
            } else if (c == b) {
                if (aCount > 0) {
                    aCount -= 1;
                    res += x;
                } else {
                    bCount += 1;
                }
            } else {
                res += Math.Min(aCount, bCount) * y;
                aCount = 0;
                bCount = 0;
            }
        }
        res += Math.Min(aCount, bCount) * y;

        return res;
    }
}
