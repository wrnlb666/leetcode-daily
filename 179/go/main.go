package main


import (
    "fmt"
    "slices"
    "strings"
    "strconv"
)


func largestNumber(nums []int) string {
    list := make([]string, len(nums))
    for i, v := range nums {
        list[i] = strconv.Itoa(v)
    }
    slices.SortFunc(list, func(i, j string) int {
        a := i + j
        b := j + i
        ia := 0
        ib := 0
        if a > b {
            ia = 1
        }
        if b > a {
            ib = 1
        }
        return ib - ia
    })
    if list[0] == "0" {
        return "0"
    }
    return strings.Join(list, "")
}


func main() {
    nums := []int{0,9,8,7,6,5,4,3,2,1}
    res := largestNumber(nums)
    fmt.Println(res)
}
