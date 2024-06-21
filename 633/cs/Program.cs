// See https://aka.ms/new-console-template for more information
int input = 5;
bool res = new Solution().JudgeSquareSum(input);
Console.WriteLine($"{res}");


public class Solution {
    public bool JudgeSquareSum(int c) {
        for (int i = 2; i * i <= c; i++) {
            int count = 0;
            while (c % i == 0) {
                c /= i;
                count += 1;
            }
            if (i % 4 == 3 && count % 2 != 0) {
                return false;
            }
        }
        return c % 4 != 3;
    }
}
