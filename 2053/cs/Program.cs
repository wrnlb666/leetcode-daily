string[] arr = ["d","b","c","b","c","a"];
int k = 2;
string res = new Solution().KthDistinct(arr, k);
Console.WriteLine(res);


public class Solution {
    public string KthDistinct(string[] arr, int k) {
        Dictionary<string, int> dict = new();
        for (int i = 0; i < arr.Length; i++) {
            string s =  arr[i];
            if (dict.ContainsKey(s)) {
                dict[s] = -1;
            } else {
                dict[s] = i;
            }
        }

        foreach (string s in arr) {
            if (dict[s] != -1) {
                k -= 1;
            }
            if (k == 0) {
                return s;
            }
        }

        return "";
    }
}
