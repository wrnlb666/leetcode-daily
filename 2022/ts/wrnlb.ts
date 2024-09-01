function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (original.length !== m * n) {
        return []
    }
    let res: number[][] = []
    for (let i = 0; i < m; i++) {
        let row: number[] = []
        for (let j = 0; j < n; j++) {
            row.push(original[i * n + j])
        }
        res.push(row)
    }
    return res
}


function main(): void {
    const original: number[] = [1,2,3,4]
    const m: number = 2
    const n: number = 2

    const res: number[][] = construct2DArray(original, m, n)
    console.log(res)
}


main()
