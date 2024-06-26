// See https://aka.ms/new-console-template for more information
TreeNode root = new(1, new(2, new(4), new(5)), new(3, new(6), new(7)));
TreeNode res = new Solution().BalanceBST(root);
Console.WriteLine(res);



// Definition for a binary tree node.
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
    public TreeNode BalanceBST(TreeNode root) {
        // get sorted list
        List<int> list = new();

        Action<TreeNode?>? Traverse = null;
        Traverse = delegate(TreeNode? curr) {
            if (curr == null) {
                return;
            }

            // traverse left
            Traverse!(curr.left);

            // append to list
            list.Add(curr.val);

            // traverse right
            Traverse!(curr.right);
        };

        Traverse(root);

        // build tree recursively
        int start = 0;
        int end = list.Count - 1;
        
        Func<int, int, TreeNode?>? Build = null;
        Build = delegate(int start, int end) {
            if (start > end) {
                return null;
            }

            int mid = (start + end) / 2;
            return new(
                    list[mid],
                    Build!(start, mid - 1),
                    Build!(mid + 1, end)
                    );
        };

        return Build(start, end)!;
    }
}
