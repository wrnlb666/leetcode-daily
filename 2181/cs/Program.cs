ListNode head = new(0, new(3, new(1, new(0, new(4, new(5, new(2, new(0, null))))))));
ListNode res = new Solution().MergeNodes(head);
res.Print();


/*Definition for singly-linked list.*/
public class ListNode {
    public int val;
    public ListNode? next;
    
    public ListNode(int val=0, ListNode? next=null) {
        this.val = val;
        this.next = next;
    }

    public void Print() {
        string s = "";
        ListNode? curr = this;
        while (curr != null) {
            s += " " + curr.val.ToString();
            curr = curr.next;
        }
        Console.WriteLine(s);
    }
}


public class Solution {
    public ListNode MergeNodes(ListNode head) {
        int sum = 0;
        ListNode? curr = head.next!;
        ListNode index = head;
        while (curr != null) {
            if (curr.val == 0) {
                index.val = sum;
                sum = 0;
                if (curr.next != null) {
                    index.next = curr;
                    index = index.next;
                } else {
                    index.next = null;
                    break;
                }
            } else {
                sum += curr.val;
            }
            curr = curr.next;
        }
        return head;
    }
}
