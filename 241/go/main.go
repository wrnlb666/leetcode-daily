package main


import (
    "fmt"
    "time"
    "regexp"
    "strconv"
)


const (
    ADD = "+"
    SUB = "-"
    MUL = "*"
)


var re = regexp.MustCompile(`[\+\-\*]`)


func add(cache map[string][]int, expr string) []int {
    time.Sleep(time.Millisecond * 100)
    fmt.Println(cache)
    if v, ok := cache[expr]; ok {
        return v
    }
    nums := re.Split(expr, -1)
    opers := re.FindAllStringIndex(expr, -1)
    // fmt.Println(nums, opers)

    if len(nums) == 1 {
        tmp, _ := strconv.Atoi(expr)
        cache[expr] = []int{tmp}
        return []int{tmp}
    }
    if len(opers) == 1 {
        left, _ := strconv.Atoi(expr[:opers[0][0]])
        right, _ := strconv.Atoi(expr[opers[0][1]:])
        oper := expr[opers[0][0]:opers[0][1]]
        switch oper {
            case ADD:
                tmp := []int{left + right}
                cache[expr] = tmp
                return tmp
            case SUB:
                tmp := []int{left - right}
                cache[expr] = tmp
                return tmp
            case MUL:
                tmp := []int{left * right}
                cache[expr] = tmp
                return tmp
        }
    }

    res := []int{}
    for i := range len(nums) - 1 {
        str := expr[:opers[i][1]-1]
        if v, ok := cache[str]; ok {
            res = append(res, v...)
        } else {
            tmp := add(cache, str)
            cache[str] = tmp
            res = append(res, v...)
        }
        str = expr[opers[i][1]:]
        if v, ok := cache[str]; ok {
            res = append(res, v...)
        } else {
            tmp := add(cache, str)
            cache[str] = tmp
            res = append(res, v...)
        }
    }

    cache[expr] = res
    return res
}


func diffWaysToCompute(expression string) []int {
    cache := make(map[string][]int)
    res := add(cache, expression)
    
    return res
}


func main() {
    expression := "2*3-4*5"
    res := diffWaysToCompute(expression)
    fmt.Println(res)
}
