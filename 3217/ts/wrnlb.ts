// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
    static fromList(l: number[]): ListNode {
        let head: ListNode = new ListNode()
        let curr: ListNode = head
        l.forEach((n) => {
            curr.next = new ListNode(n)
            curr = curr.next
        })
        return head.next!
    }
    toList(): number[] {
        let l: number[] = []
        for (let curr: ListNode | null = this; curr != null; curr = curr.next) {
            l.push(curr.val)
        }
        return l
    }
}


function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    let numSet: Set<number> = new Set(nums)
    for (let curr = head; numSet.has(curr!.val); curr = curr!.next) {
        head = head!.next
    }
    let prev: ListNode | null = head
    let curr: ListNode | null = head!.next
    for (; curr != null;) {
        if (numSet.has(curr!.val)) {
            prev!.next = curr.next
            curr = curr.next
            continue
        }
        prev = curr
        curr = curr.next
    }
    return head
}


(() => {
    const nums: number[] = [1,7,6,2,4]
    const head: number[] = [3,7,1,8,1]

    const res: ListNode | null = modifiedList(nums, ListNode.fromList(head))
    console.log(res?.toList())
})()
