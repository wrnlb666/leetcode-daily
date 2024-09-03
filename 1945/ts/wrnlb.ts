function getLucky(s: string, k: number): number {
    let sum: number = 0
    for (let i = 0; i < s.length; i++) {
        let num = s.charCodeAt(i) - 96
        if (num < 10) {
            sum += num
        } else {
            sum += ~~(num / 10)
            sum += num % 10
        }
    }
    for (let c = 1; c < k; c++) {
        let newSum = 0
        while (sum > 0) {
            newSum += sum % 10
            sum = ~~(sum / 10)
        }
        sum = newSum
    }
    return sum
}


(() => {
    const s: string = "leetcode"
    const k: number = 2
    const res: number = getLucky(s, k)
    console.log(res)
})()
