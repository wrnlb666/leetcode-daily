

int k = 3;
int w = 0;
int[] profits = {1,2,3};
int[] capital = {0,1,2};
Console.WriteLine(new Solution().FindMaximizedCapital(k, w, profits, capital));

public class Solution {
    public int FindMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.Length;

        PriorityQueue<ValueTuple<int, int>, int> combine = new();
        for (int i = 0; i < n; i++) {
            combine.Enqueue((capital[i], profits[i]), capital[i]);
        }

        PriorityQueue<int, int> cache = new();
        for (int i = 0; i < k; i++) {
            while (combine.Count != 0 && combine.Peek().Item1 <= w) {
                (_, int p) = combine.Dequeue();
                cache.Enqueue(p, -p);
            }
            if (cache.Count == 0) {
                break;
            }
            w += cache.Dequeue();
        }
        
        return w;
    }
}
