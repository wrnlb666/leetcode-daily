function missingRolls(rolls: number[], mean: number, n: number): number[] {
    // calculate sum of `n` nubmers
    const m: number = rolls.length
    let sum: number = 0
    rolls.forEach((r) => {
        sum += r
    })
    const total: number = mean * (m + n)
    sum = total - sum

    // find a possible solution to consume sum
    let nMean: number = sum / n
    if (nMean > 6 || nMean < 1) {
        return []
    }
    nMean = ~~nMean
    let remainder: number = sum % n
    let res: number[] = new Array(n)
    const gap: number = 6 - nMean
    const count: number = ~~(remainder / gap)
    remainder = remainder % gap
    let i = 0
    for (; i < count; i++) {
        res[i] = 6
    }
    if (!Number.isNaN(remainder)) {
        res[i++] = nMean + remainder
    }
    for (; i < n; i++) {
        res[i] = nMean
    }
    return res
}


(() => {
    const rolls: number[] = [3,2,4,3]
    const mean: number = 4
    const n: number = 2

    const res: number[] = missingRolls(rolls, mean, n)
    console.log(res)
})()
