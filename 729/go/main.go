package main


import (
    "fmt"
)


type Node struct {
    start   int
    end     int
    left    *Node
    right   *Node
}


type MyCalendar struct {
    bst     *Node
}


func Constructor() MyCalendar {
    return MyCalendar{}
}


func (this *MyCalendar) Book(start int, end int) bool {
    if this.bst == nil {
        this.bst = &Node{
            start: start,
            end: end,
        }
        return true
    }
    node := this.bst
    for {
        if end <= node.start {
            if node.left == nil {
                node.left = &Node{
                    start: start,
                    end: end,
                }
                return true
            } else {
                node = node.left
                continue
            }
        } else if start >= node.end {
            if node.right == nil {
                node.right = &Node{
                    start: start,
                    end: end,
                }
                return true
            }
        } else {
            return false
        }
    }
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */


func main() {
    res := []bool{}
    cal := Constructor()
    res = append(res, cal.Book(10, 20))
    res = append(res, cal.Book(15, 25))
    res = append(res, cal.Book(20, 30))
    fmt.Println(res)
}
