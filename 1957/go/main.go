package main


import (
    "fmt"
)


func makeFancyString(s string) string {
    res := []byte{}
    last := [2]byte{}
    for _, c := range []byte(s) {
        if c == last[0] {
            if c == last[1] {
                continue
            } else {
                last[1] = c
                res = append(res, c)
            }
        } else {
            last[0] = c
            last[1] = 0
            res = append(res, c)
        }
    }
    return string(res)
}


func main() {
    s := "leeetcode"
    res := makeFancyString(s)
    fmt.Println(res)
}
