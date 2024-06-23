package main

import (
    "fmt"
    "container/heap"
)

type tuple [2]int

type hq []tuple

func (h hq) Len() int {
    return len(h)
}

func (h hq) Less(i, j int) bool {
    return h[i][0] < h[j][0]
}

func (h hq) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h *hq) Push(x interface{}) {
    *h = append(*h, x.(tuple))
}

func (h *hq) push(t tuple) {
    h.Push(t)
}

func (h *hq) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func (h *hq) pop() tuple {
    return h.Pop().(tuple)
}

func (h hq) peak() tuple {
    return h[0]
}

func longestSubarray(nums []int, limit int) int {
    minHeap := hq{}
    maxHeap := hq{}

    left := 0
    maxLength := 0

    for right, v := range(nums) {
        heap.Push(&minHeap, tuple{v, right})
        heap.Push(&maxHeap, tuple{-v, right})

        for -maxHeap[0][0] - minHeap[0][0] > limit {
            left = min(maxHeap[0][1], minHeap[0][1]) + 1

            for maxHeap[0][1] < left {
                heap.Pop(&maxHeap)
            }
            for minHeap[0][1] < left {
                heap.Pop(&minHeap)
            }
        }

        maxLength = max(maxLength, right - left + 1)
    }

    return maxLength
}


func main() {
    nums := []int{4,2,2,2,4,4,2,2}
    limit := 0
    res := longestSubarray(nums, limit)
    fmt.Println(res)
}
