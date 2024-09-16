package main


import (
    "fmt"
    "slices"
)


func findMinDifference(timePoints []string) int {
    // convert to int
    length := len(timePoints)
    minutes := make([]int, length + 1)
    for i, s := range timePoints {
        hrs := 0
        mns := 0
        isH := true
        for _, c := range s {
            if c == ':' {
                isH = false
                continue
            }
            if isH == true {
                hrs = hrs * 10 + (int(c) - 0x30)
            } else {
                mns = mns * 10 + (int(c) - 0x30)
            }
        }
        minutes[i] = hrs * 60 + mns
    }

    // sort
    slices.Sort(minutes[:length])
    minutes[length] = minutes[0] + 1440
    
    // compare and get the smallest difference
    res := minutes[1] - minutes[0]
    for i := range length {
        res = min(res, minutes[i + 1] - minutes[i])
    }

    return res
}


func main() {
    timePoints := []string{"23:59","00:00"}
    res := findMinDifference(timePoints)
    fmt.Println(res)
}
