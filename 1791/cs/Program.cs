int[][] edges = [[1,2],[2,3],[4,2]];
int res = new Solution().FindCenter(edges);
Console.WriteLine(res);


public class Solution {
    public int FindCenter(int[][] edges) {
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges[0][0] : edges[0][1];
    }
}
