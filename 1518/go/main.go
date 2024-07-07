package main


import (
    "fmt"
)


func main() {
    numBottles := 15
    numExchange := 4

    res := numWaterBottles(numBottles, numExchange)
    fmt.Println(res)
}


func numWaterBottles(numBottles int, numExchange int) int {
    res := numBottles
    full := 0

    for numBottles >= numExchange {
        full = numBottles / numExchange
        numBottles = numBottles % numExchange
        numBottles += full
        res += full
    }

    return res
}
