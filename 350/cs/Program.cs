int[] nums1 = [1,2,2,1];
int[] nums2 = [2,2];
int[] res = new Solution().Intersect(nums1, nums2);
Console.WriteLine(String.Join(" ", res));


public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);

        int i1 = 0;
        int i2 = 0;
        List<int> res = new();

        for (;i1 < nums1.Length && i2 < nums2.Length;) {
            if (nums1[i1] == nums2[i2]) {
                res.Add(nums1[i1]);
                i1++;
                i2++;
            } else if (nums1[i1] < nums2[i2]) {
                i1++;
            } else {
                i2++;
            }
        }

        return res.ToArray();
    }
}
