class unionFind {
    public count: number
    private parent: number[]
    constructor(n: number) {
        this.count = n
        this.parent = new Array(n).fill(-1)
    }
    public find(index: number): number {
        if (this.parent[index] < 0) {
            return index
        }
        return this.find(this.parent[index])
    }
    public union(n1: number, n2: number) {
        let r1 = this.find(n1)
        let r2 = this.find(n2)
        if (r1 === r2) {
            return
        }
        this.parent[r1] = r2
        this.count -= 1
    }
    public getCount(): number {
        return this.count
    }
}


function removeStones(stones: number[][]): number {
    let uf: unionFind = new unionFind(stones.length)
    for (let i = 0; i < stones.length; i++) {
        for (let j = i + 1; j < stones.length; j++) {
            if (stones[i][0] === stones[j][0] || stones[i][1] === stones[j][1]) {
                uf.union(i, j)
            }
        }
    }
    return stones.length - uf.getCount()
};


function main() {
    const stones: number[][] = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    const res: number = removeStones(stones)
    console.log(res)
}


main()
