// Definition for node.
class _Node {
    val: number
    children: _Node[]
    constructor(val?: number) {
        this.val = (val===undefined ? 0 : val)
        this.children = []
    }
    static fromList(lst: (number|null)[]): _Node {
        class queue {
            private items: _Node[] = []
            enqueue(item: _Node) {
                this.items.push(item)
            }
            dequeue(): _Node {
                return this.items.shift()!
            }
            size(): number {
                return this.items.length
            }
        }    
        let first: number|null|undefined = lst.shift()
        if (first === undefined || first === null) {
            return new _Node()
        }
        lst.shift()!
        let root: _Node = new _Node(first)
        let q: queue = new queue()
        q.enqueue(root)
        while (lst.length != 0) {
            let node: _Node = q.dequeue()
            let n: number|null|undefined = lst.shift()
            while (n !== null && n != undefined) {
                let child: _Node = new _Node(n)
                node.children.push(child)
                q.enqueue(child)
                n = lst.shift()
            }
        }
        return root
    }
}


/**
 * Definition for node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function postorder(root: _Node | null): number[] {
    if (root === null) {
        return []
    }
    let res: number[] = []
    function dfs(node: _Node) {
        for (let child of node.children) {
            dfs(child)
        }
        res.push(node.val)
    }
    dfs(root)
    return res
}


function main() {
    let lst: (number|null)[] = [1,null,3,2,4,null,5,6]
    let root: _Node = _Node.fromList(lst)
    let res: number[] = postorder(root)
    console.log(res)
}


main()
