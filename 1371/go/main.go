package main


import (
    "slices"
)


func findTheLongestSubstring(s string) int {
    chars := [26]int{}
    chars['a' - 'a'] = 1 << 0
    chars['e' - 'a'] = 1 << 1
    chars['i' - 'a'] = 1 << 2
    chars['o' - 'a'] = 1 << 3
    chars['u' - 'a'] = 1 << 4

    curr := 0
    mp := slices.Repeat([]int{-1}, 1 << 5)
    res := 0
    for i, v := range s {
        curr ^= chars[v - 'a']
        if mp[curr] == -1 && curr != 0 {
            mp[curr] = i
        }
        res = max(res, i - mp[curr])
    }
    return res
}


func main() {
    s := "yopumzgd"
    res := findTheLongestSubstring(s)
    println(res)
}
