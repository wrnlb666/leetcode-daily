package main


import (
    "fmt"
)


func dividePlayers(skill []int) int64 {
    count := make(map[int]int)
    total := 0
    for _, v := range skill {
        if _, ok := count[v]; ok {
            count[v] += 1
        } else {
            count[v] = 1
        }
        total += v
    }
    score := total / (len(skill) / 2)
    
    res := int64(0)
    for k, v := range count {
        if v == 0 {
            continue
        }
        for count[k] != 0 {
            count[k] -= 1
            if c, ok := count[score - k]; ok {
                if c == 0 {
                    return -1
                }
                count[score - k] -= 1
                res += int64(k) * int64(score - k)
            } else {
                return -1
            }
        }
    }

    return res
}


func main() {
    skill := []int{2,4,1,3}
    res := dividePlayers(skill)
    fmt.Println(res)
}
