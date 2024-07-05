int[] list = [2,2,1,3];
ListNode head = new(list);
int[] res = new Solution().NodesBetweenCriticalPoints(head);
Console.WriteLine(string.Join(" ", res));


// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode? next;

    public ListNode(int val=0, ListNode? next=null) {
        this.val = val;
        this.next = next;
    }

    public ListNode(int[] arr) {
        if (arr.Length == 0) return;
        this.val = arr[0];
        ListNode p = this;
        for (int i = 1; i < arr.Length; i++) {
            p.next = new ListNode(arr[i]);
            p = p.next;
        }
    }

    public void Print() {
        string s = "";
        for (ListNode? node = this; node != null; node = node.next) {
            s += " " + node.val.ToString();
        }
        Console.WriteLine(s);
    }
}

public class Solution {
    public int[] NodesBetweenCriticalPoints(ListNode head) {
        int[] res = [int.MaxValue, -1];
        int index = 1;
        ListNode? prevNode = head;
        ListNode? currNode = head.next;
        // initialize CP to untrue state
        int firstCP = -1;
        int prevCP = -1;

        for (; currNode!.next != null; prevNode = currNode, currNode = currNode.next, index += 1) {
            // check if curr is critical point
            if ((prevNode.val < currNode.val && currNode.next.val < currNode.val) ||
                (prevNode.val > currNode.val && currNode.next.val > currNode.val)) {
                if (firstCP == -1) {
                    firstCP = index;
                    prevCP = index;
                } else {
                    res[0] = Math.Min(res[0], index - prevCP);
                    prevCP = index;
                }
            }
        }

        if (firstCP == prevCP) {
            res = [-1, -1];
        } else {
            res[1] = prevCP - firstCP;
        }
        
        return res;
    }
}
