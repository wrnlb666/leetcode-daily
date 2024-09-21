package main

import (
    "fmt"
)


func lexicalOrder(n int) []int {
    if n == 0 {
        return []int{0}
    }
    res := []int{}
    var dfs func(curr int)
    dfs = func(curr int) {
        curr *= 10
        for i := range 10 {
            next := curr + i
            if next <= n {
                res = append(res, next)
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
            res = append(res, next)
            dfs(next)
        } else {
            break
        }
    }

    return res
}


func main() {
    n := 0
    res := lexicalOrder(n)
    fmt.Println(res)
}
