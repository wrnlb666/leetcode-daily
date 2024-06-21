// See https://aka.ms/new-console-template for more information

int[] customers = { 1, 0, 1, 2, 1, 1, 7, 5 };
int[] grumpy = { 0, 1, 0, 1, 0, 1, 0, 1 };
int minutes = 3;
int res = new Solution().MaxSatisfied(customers, grumpy, minutes);

Console.WriteLine(res);

public class Solution {
    public int MaxSatisfied(int[] customers, int[] grumpy, int minutes) {
        Func<int, int> UsePower = delegate(int i) {
            return customers[i];
        };
        Func<int,int> NoPower = (i) => {
            if (grumpy[i] == 0) {
                return customers[i];
            } else {
                return 0;
            }
        };

        int winPower = 0;
        int winNopow = 0;

        // first win
        for (int i = 0; i < minutes; i++) {
            winPower += UsePower(i);
            winNopow += NoPower(i);
        }

        ValueTuple<int, int> good = (0, winPower - winNopow);

        int length = customers.Length;
        for (int i = 1; i < length - minutes + 1; i++) {
            winPower = winPower - UsePower(i - 1) + UsePower(i + minutes - 1);
            winNopow = winNopow - NoPower(i - 1) + NoPower(i + minutes - 1);
            int temp = winPower - winNopow;
            good = good.Item2 > temp ? good : (i, temp);
        }

        for (int i = good.Item1; i < good.Item1 + minutes; i++) {
            grumpy[i] = 0;
        }

        int res = 0;
        for (int i = 0; i < length; i++) {
            if (grumpy[i] == 0) {
                res += customers[i];
            }
        }

        return res;
    }
}
