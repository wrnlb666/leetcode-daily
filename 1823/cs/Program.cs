int n = 6;
int k = 5;
int res = new Solution().FindTheWinner(n, k);
Console.WriteLine(res);


public class Solution {
    public int FindTheWinner(int n, int k) {
        CircularList list = new();
        list.Capacity = n;
        for (int i = 1; i <= n; i++) {
            list.Add(i);
        }
        
        int index = 0;
        while (list.Count > 1) {
            index = (index + k - 1) % list.Count;
            list.RemoveAt(index);
        }
        return list[0];
    }
}

class CircularList : List<int> {
    public CircularList() : base() {}
    public CircularList(List<int> list) : base(list) {}

    public new int this[int index] {
        get {
            if (index >= Count) {
                index %= Count;
            }
            return base[index];
        }
        set {
            if (index >= Count) {
                index %= Count;
            }
            base[index] = value;
        }
    }
}
