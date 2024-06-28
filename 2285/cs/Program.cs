int n = 5;
int[][] roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]];
long res = new Solution().MaximumImportance(n, roads);
Console.WriteLine(res);


public class Solution {
    public long MaximumImportance(int n, int[][] roads) {
        long[] count = new long[n];
        foreach (int[] road in roads) {
            foreach (int v in road) {
                count[v] += 1;
            }
        }

        long res = 0;
        Array.Sort(count);
        for (long i = 0; i < count.Length; i++) {
            res += count[i] * (i + 1);
        }

        return res;
    }
}
