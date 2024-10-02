package main

import (
	"fmt"
	"slices"
)


func arrayRankTransform(arr []int) []int {
    if len(arr) == 0 {
        return arr
    }
    res := slices.Clone(arr)
    slices.Sort(arr)
    cache := make(map[int]int)
    cache[arr[0]] = 1
    currN := arr[0]
    currI := 1
    for _, v := range arr[1:] {
        if v != currN {
            currN = v
            currI += 1
            cache[currN] = currI
        }
    }
    for i, v := range res {
        res[i] = cache[v]
    }
    return res
}


func main() {
    arr := []int{37,12,28,9,100,56,80,5,12}
    res := arrayRankTransform(arr)
    fmt.Println(res)
}
