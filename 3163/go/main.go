package main

import (
	"fmt"
	"strconv"
	"strings"
)


func compressedString(word string) string {
    last := 'A'
    count := 0
    res := strings.Builder{}
    for _, w := range word {
        if w == last {
            count += 1
            if count == 9 {
                res.WriteString(strconv.Itoa(count) + string(last))
                last = 'A'
                count = 0
            }
        } else {
            if count != 0 {
                res.WriteString(strconv.Itoa(count) + string(last))
            }
            last = w
            count = 1
        }
    }
    if count != 0 {
        res.WriteString(strconv.Itoa(count) + string(last))
    }
    return res.String()
}


func main() {
    word := "aaaaaaaaaaaaaabb"
    res := compressedString(word)
    fmt.Println(res)
}
