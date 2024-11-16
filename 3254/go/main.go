package main


import (
    "fmt"
    // "slices"
)


func resultsArray(nums []int, k int) []int {
    if k == 1 {
        return nums
    }
    res := make([]int, len(nums) - k + 1)
    index := 0
    last := nums[0]
    consecutive := 1
    for _, v := range nums[1:k] {
        if v == last + 1 {
            consecutive += 1
        } else {
            consecutive = 1
        }
        last = v
    }
    if consecutive != k {
        res[index] = -1
        index += 1
    } else {
        res[index] = last
        index += 1
    }
    for _, v := range nums[k:] {
        if v == last + 1 {
            consecutive += 1
        } else {
            consecutive = 1
        }
        if consecutive >= k {
            res[index] = v
            index += 1
        } else {
            res[index] = -1
            index += 1
        }
        last = v
    }

    return res
}


func main() {
    nums := []int{197,198,87,88,89,90,182,103,37,80}
    k := 3

    res := resultsArray(nums, k)
    fmt.Println(res)
}
