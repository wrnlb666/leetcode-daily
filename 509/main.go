package main

import (
	"fmt"
)

func fib(n int) int {
    buf := map[int]int{}

    var warp func(n int) int
    warp = func(n int) int {
        if v, ok := buf[n]; ok {
            return v
        }
        if n < 2 {
            buf[n] = n
            return n
        }
        buf[n] = warp(n-1) + warp(n-2)
        return buf[n]
    }

    return warp(n)
}

func main() {
    fmt.Println(fib(4))
}
