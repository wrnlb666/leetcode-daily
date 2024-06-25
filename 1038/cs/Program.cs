// See https://aka.ms/new-console-template for more information
TreeNode root = new(4, new(1, new(0), new(2, null, new(3))), new(6, new(5), new(7, null, new(8))));
TreeNode res = new Solution().BstToGst(root);
Console.WriteLine(res.ToString());


/*Definition for a binary tree node.*/
public class TreeNode {
    public int val;
    public TreeNode? left;
    public TreeNode? right;
    public TreeNode(int val=0, TreeNode? left=null, TreeNode? right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


public class Solution {
    public TreeNode BstToGst(TreeNode root) {
        int sum = 0;

        Action<TreeNode?>? PrefixSum = null;
        PrefixSum = delegate(TreeNode? curr) {
            if (curr == null || PrefixSum == null) {
                return;
            }

            // apply larger
            PrefixSum(curr.right);

            // apply current
            int temp = curr.val;
            curr.val += sum;
            sum += temp;

            // apply smaller
            PrefixSum(curr.left);
        };

        PrefixSum(root);

        return root;
    }
}
