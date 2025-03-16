package main

import (
	"fmt"
	"math"
)

func cal(ranks []int, t int64) int {
	var total int = 0
	for _, r := range ranks {
		var temp float64 = float64(t / int64(r))
		total += int(math.Sqrt(temp))
	}
	return total
}

func repairCars(ranks []int, cars int) int64 {
	var (
		left  int64 = 1
		right int64 = int64(cars) * int64(cars) * int64(ranks[0])
	)

	for left < right {
		var mid int64 = (left + right) / 2
		total := cal(ranks, mid)
		if total < cars {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}

func main() {
	ranks := []int{4, 2, 3, 1}
	cars := 10
	res := repairCars(ranks, cars)
	fmt.Println(res)
}
