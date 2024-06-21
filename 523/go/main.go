package main


import (
    "fmt"
)

func checkSubarraySum(nums []int, k int) bool {
    rm := map[int]int{0: -1}
    sum := 0

    for i, v := range nums {
        sum += v
        r := sum % k
        if tmp, ok := rm[r]; ok {
            if i - tmp > 1 {
                return true
            }
        } else {
            rm[r] = i
        }
    }

    return false
}

func main() {
    nums := []int{23,2,4,6,7}
    k := 6
    fmt.Println(checkSubarraySum(nums, k))
}
