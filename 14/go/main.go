package main


import (
    "fmt"
)


func longestCommonPrefix(strs []string) string {
    res := ""
    length := 200
    for _, v := range strs {
        length = min(length, len(v))
    }
    loop: for i := range length {
        curr := strs[0][i]
        for _, s := range strs[1:] {
            if s[i] != curr {
                break loop
            }
        }
        res += string(curr)
    }
    return res
}


func main() {
    strs := []string{"flower","flow","flight"}
    res := longestCommonPrefix(strs)
    fmt.Println(res)
}
