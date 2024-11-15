package main


import (
    "fmt"
)


func findLengthOfShortestSubarray(arr []int) int {
    right := len(arr) - 1
    for ; right > 0 && arr[right] >= arr[right-1]; right -= 1 {}

    res := right
    left := 0
    for left < right && (left == 0 || arr[left - 1] <= arr[left]) {
        for ; right < len(arr) && arr[left] > arr[right]; right += 1 {}
        res = min(res, right - left - 1)
        left += 1
    }
    return res
}


func main() {
    arr := []int{1,2,3,10,0,7,8,9}
    
    res := findLengthOfShortestSubarray(arr)
    fmt.Println(res)
}
