package main

import (
    "fmt"
)


func findKthNumber(n int, k int) int {
    if k == 0 {
        return 0
    }
    res := 0
    var dfs func(curr int)
    dfs = func(curr int) {
        curr *= 10
        for i := range 10 {
            next := curr + i
            if next <= n {
                if k == 0 {
                    return
                }
                res = next
                k -= 1
                dfs(next)
            } else {
                return
            }
        }
    }
    
    curr := 0
    for i := range 9 {
        next := curr + i + 1
        if next <= n {
            if k == 0 {
                break
            }
            res = next
            k -= 1
            dfs(next)
        } else {
            break
        }
    }

    return res
}


func main() {
    n := 957747794
    k := 424238336
    res := findKthNumber(n, k)
    fmt.Println(res)
}
