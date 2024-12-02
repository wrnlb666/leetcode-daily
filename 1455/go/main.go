package main


import (
    "fmt"
)


func isPrefixOfWord(sentence string, searchWord string) int {
    curr := 1
    skip := false
    index := 0
    
    for i := range len(sentence) {
        v := sentence[i]
        if v == ' ' {
            skip = false
            curr += 1
            index = 0
            continue
        }
        if skip {
            continue
        }
        if v != searchWord[index] {
            skip = true
            continue
        }
        if index == len(searchWord)-1 {
            return curr
        }
        index += 1
    }
    return -1
}


func main() {
    sentence := "corona dream"
    searchWord := "d"

    res := isPrefixOfWord(sentence, searchWord)
    fmt.Println(res)
}
