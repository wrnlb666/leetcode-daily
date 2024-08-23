package main


import (
    "fmt"
)


const (
    POS rune = '+'
    NEG = '-'
    DIV = '/'
)


type fraction struct {
    num     int
    den     int
}


func parseExpression(expression string) []fraction {
    res := []fraction{}
    pos := 1
    num := 0
    frac := fraction{}
    for i, c := range expression {
        switch c {
        case '+':
            frac.den = num
            num = 0
            res = append(res, frac)
            frac = fraction{}
            pos = 1
        case '-':
            if i != 0 {
                frac.den = num
                num = 0
                res = append(res, frac)
            }
            frac = fraction{}
            pos = -1
        case '/':
            frac.num = num * pos
            num = 0
        case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
            num = num * 10 + int(c - '0')
        }
    }
    frac.den = num
    res = append(res, frac)
    return res
}


func findGCD(a, b int) int {
    if a == 0 {
        return b
    }
    return findGCD(b % a, a)
}


func fractionAddition(expression string) string {
    fracs := parseExpression(expression)
    
    num := 0
    den := 1
    for _, f := range fracs {
        num = num * f.den + den * f.num
        den = den * f.den
    }

    gcd := findGCD(num, den)
    if gcd < 0 {
        gcd = -gcd
    }

    return fmt.Sprintf("%d/%d", num / gcd, den / gcd)
}


func main() {
    expression := "-1/2+1/2"
    res := fractionAddition(expression)
    fmt.Println(res)
}
