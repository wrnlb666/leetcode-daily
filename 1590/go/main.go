package main


import (
    "fmt"
)


func minSubarray(nums []int, p int) int {
    prefix := make([]int, len(nums))
    sum := 0
    for i, v := range nums {
        prefix[i] = sum + v
        sum += v
    }
    target := prefix[len(prefix)-1] % p
    if target == 0 {
        return 0
    }

    dict := map[int]int {
        0: -1,
    }

    minLen := len(nums)
    for i, v := range prefix {
        v %= p
        needed := (v - target + p) % p
        if index, ok := dict[needed]; ok {
            minLen = min(minLen, i - index)
        }
        dict[v] = i
    }
    if minLen == len(nums) {
        return -1
    }
    return minLen
}


func main() {
    nums := []int{3,1,4,2}
    p := 6
    res := minSubarray(nums, p)
    fmt.Println(res)
}
