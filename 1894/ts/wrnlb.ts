function chalkReplacer(chalk: number[], k: number): number {
    let sum: number = 0
    for (let i = 0; i < chalk.length; i++) {
        sum += chalk[i]
        if (sum > k) {
            return i
        }
    }
    k %= sum
    sum = 0
    for (let i = 0; i < chalk.length; i++) {
        sum += chalk[i]
        if (sum > k) {
            return i
        }
    }
    return 0
}


(() => {
    const chalk: number[] = [3,4,1,2]
    const k: number = 25
    const res: number = chalkReplacer(chalk, k)
    console.log(res)
})()
