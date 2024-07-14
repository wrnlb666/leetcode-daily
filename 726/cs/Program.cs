string formula = "((HHe28Be26He)9)34";
string res = new Solution().CountOfAtoms(formula);
Console.WriteLine(res);


public class Solution {
    // public static void Debug(Dictionary<string, int> dict) {
    //     Console.WriteLine(String.Join(" ", dict));
    // }

    public static void Combine(Dictionary<string, int> dst, Dictionary<string, int> src) {
        foreach (var kv in src) {
            if (dst.ContainsKey(kv.Key)) {
                dst[kv.Key] += kv.Value;
            } else {
                dst[kv.Key] = kv.Value;
            }
        }
    }

    public static void Multiply(Dictionary<string, int> dict, int multiplier) {
        foreach (var k in dict.Keys) {
            dict[k] *= multiplier;
        }
    }

    public static Dictionary<string, int> Rec(string formula, ref int i) {
        Dictionary<string, int> res = new();
        string? curr = null;
        int count = 0;

        for (; i < formula.Length; i++) {
            char c = formula[i];
            if (c == '(') {
                i += 1;
                var dict = Rec(formula, ref i);
                Combine(res, dict);
            } else if (c == ')') {
                if (curr != null) {
                    if (count == 0) count = 1;
                    if (res.ContainsKey(curr!)) {
                        res[curr!] += count;
                    } else {
                        res[curr!] = count;
                    }
                }
                count = 0;
                while (i + 1 < formula.Length && Char.IsNumber(formula[i+1])) {
                    char tmp = formula[i+1];
                    count = count * 10 + (int)tmp - 48;
                    i += 1;
                }
                if (count != 0) {
                    Multiply(res, count);
                }
                return res;
            } else if (Char.IsUpper(c)) {
                if (curr != null) {
                    if (count == 0) count = 1;
                    if (res.ContainsKey(curr)) {
                        res[curr] += count;
                    } else {
                        res[curr] = count;
                    }
                    count = 0;
                }
                curr = c.ToString();
            } else if (Char.IsLower(c)) {
                curr += c;
            } else if (Char.IsNumber(c)) {
                count = count * 10 + (int)c - 48;
            }
        }

        if (curr != null) {
            if (count == 0) count = 1;
            if (res.ContainsKey(curr)) {
                res[curr] += count;
            } else {
                res[curr] = count;
            }
        }

        return res;
    }

    public string CountOfAtoms(string formula) {
        int recIndex = 0;
        Dictionary<string, int> dict = Rec(formula, ref recIndex);
        List<string> keys = new(dict.Keys);
        keys.Sort();

        string res = "";
        foreach (var k in keys) {
            if (dict[k] == 1) {
                res += $"{k}";
            } else {
                res += $"{k}{dict[k]}";
            }
        }

        return res;
    }
}
