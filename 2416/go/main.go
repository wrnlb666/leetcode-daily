package main


import (
    "fmt"
    "strconv"
)


type Node struct {
    score   int
    child   map[rune]*Node
}


func sumPrefixScores(words []string) []int {
    tire := &Node{
        score: 0,
        child: map[rune]*Node{},
    }
    for _, word := range words {
        node := tire
        for _, char := range word {
            if n, ok := node.child[char]; ok {
                node = n
                node.score += 1
            } else {
                node.child[char] = &Node{
                    score: 1,
                    child: map[rune]*Node{},
                }
                node = node.child[char]
            }
        }
    }

    res := make([]int, len(words))
    for i, word := range words {
        node := tire
        for _, char := range word {
            node = node.child[char]
            res[i] += node.score
        }
    }

    return res
}


func main() {
    words := []string{"abc","ab","bc","b"}
    res := sumPrefixScores(words)
    fmt.Println(res)
}
