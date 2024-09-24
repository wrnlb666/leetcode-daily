package main


import (
    "fmt"
)


type void struct{}


func populateArr(arr []int) map[int]void {
    res := make(map[int]void)
    for _, v := range arr {
        if v == 0 {
            res[v] = void{}
        }
        for v > 0 {
            res[v] = void{}
            v /= 10
        }
    }
    return res
}


func getLen(n int) int {
    if n == 0 {
        return 1
    }
    res := 0
    for ; n > 0; res += 1 {
        n /= 10
    }
    return res
}


func longestCommonPrefix(arr1 []int, arr2 []int) int {
    prefix := populateArr(arr1)

    res := 0
    for _, v := range arr2 {
        for {
            if _, ok := prefix[v]; ok {
                l := getLen(v)
                res = max(res, l)
                break
            }
            v /= 10
            if v <= 0 {
                break
            }
        }
    }
    return res
}


func main() {
    arr1 := []int{1,10,100}
    arr2 := []int{1000}
    res := longestCommonPrefix(arr1, arr2)
    fmt.Println(res)
}
