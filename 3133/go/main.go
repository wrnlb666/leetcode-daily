package main


import (
    "fmt"
)


func minEnd(n int, x int) int64 {
	index := 0
	n -= 1
	for n > 0 {
		current := n & 1
		for x & (1 << index) > 0 {
			index++
		}
		if current == 1 {
			x = x | (1 << index)
		}
		index++
		n >>= 1
	}
	return int64(x)
}


func main() {
    n := 3
    x := 4

    res := minEnd(n, x)
    fmt.Println(res)
}
