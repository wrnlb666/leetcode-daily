package main


import (
    "fmt"
)


func longestSubarray(nums []int) int {
    largest := 0
    count := 0
    curr := 0
    for _, v := range nums {
        if v < largest {
            if curr > count {
                count = curr
            }
            curr = 0
            continue
        }
        if v == largest {
            curr += 1
            continue
        }
        if v > largest {
            largest = v
            count = 0
            curr = 1
        }
    }
    if curr > count {
        return curr
    }
    return count
}


func main() {
    nums := []int{1,2,3,3,2,2}
    res := longestSubarray(nums)
    fmt.Println(res)
}
