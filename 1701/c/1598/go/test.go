package main


import (
    "fmt"
)


func minOperations(logs []string) int {
    depth := 0
    for _, a := range logs {
        switch a {
        case "../":
            if depth > 0 {
                depth--
            }
        case "./":
        default:
            depth++
        }
    }
    return depth
}


func main() {
    logs := []string{"d1/","d2/","../","d21/","./"}
    res := minOperations(logs)

    fmt.Println(res)
}
