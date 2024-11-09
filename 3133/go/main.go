package main


import (
    "fmt"
)


func minEnd(n int, x int) int64 {
    n -= 1
    if n == 0 {
        return int64(x)
    }

    cycle := []int{}
    end := x + 1
    total := 0
    last := x
    gap := 1
    for range n {
        gap = 1
        for x & (last + gap) < x {
            gap += 1
        }
        cycle = append(cycle, gap)
        last = last + gap
        total += gap
        if gap == end {
            break
        }
    }

    if n == len(cycle) {
        return int64(last)
    }

    res := int64(x)
    quotient := n / len(cycle)
    res += int64(quotient * total)
    remainder := n % len(cycle)
    for i := range remainder {
        res += int64(cycle[i])
    }

    return res
}


func main() {
    n := 3
    x := 4

    res := minEnd(n, x)
    fmt.Println(res)
}
