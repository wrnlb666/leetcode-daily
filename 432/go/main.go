package main


import (
    "fmt"
)


type node struct {
    freq    int
    name    string
    prev    *node
    next    *node
}


type AllOne struct {
    items   map[string]*node
    head    *node
    tail    *node
}


func Constructor() AllOne {
    return AllOne{
        items:  map[string]*node{},
        head:   nil,
        tail:   nil,
    }
}


func (this *AllOne) Inc(key string) {
    if n, ok := this.items[key]; !ok {
        n = &node{
            freq: 1,
            name: key,
            prev: nil,
            next: this.head,
        }
        if this.head != nil {
            this.head.prev = n
            this.head = n
        } else {
            this.head = n
            this.tail = n
        }
        this.items[key] = n
    } else {
        n.freq += 1
        if n.next == nil {
            return
        }
        tmp := n.next
        for tmp != nil {
            if tmp.freq > n.freq {
                break
            }
            tmp = tmp.next
        }
        if tmp != n.next {
            if n == this.head {
                this.head = n.next
            }
            if n.prev != nil {
                n.prev.next = n.next
            }
            n.next.prev = n.prev
            if tmp == nil {
                this.tail.next = n
                n.prev = this.tail
                this.tail = n
                n.next = nil
            } else {
                tmp.prev.next = n
                n.prev = tmp.prev
                n.next = tmp
                tmp.prev = n
            }
        }
    }
}


func (this *AllOne) Dec(key string) {
    n := this.items[key]
    n.freq -= 1
    if n.freq == 0 {
        delete(this.items, key)
        if len(this.items) == 0 {
            this.head = nil
            this.tail = nil
        } else {
            if n == this.head {
                this.head = n.next
            }
            if n == this.tail {
                this.tail = n.prev
            }
            if n.prev != nil {
                n.prev.next = n.next
            }
            if n.next != nil {
                n.next.prev = n.prev
            }
        }
        return
    }
    if n.prev == nil {
        return
    }
    tmp := n.prev
    for tmp != nil {
        if tmp.freq < n.freq {
            break
        }
        tmp = tmp.prev
    }
    if tmp != n.prev {
        if n == this.tail {
            this.tail = n.prev
        }
        if n.next != nil {
            n.next.prev = n.prev
        }
        n.prev.next = n.next
        if tmp == nil {
            this.head.prev = n
            n.next = this.head
            this.head = n
            n.prev = nil
        } else {
            tmp.next.prev = n
            n.next = tmp.next
            n.prev = tmp
            tmp.next = n
        }
    }
}


func (this *AllOne) GetMaxKey() string {
    if this.tail != nil {
        return this.tail.name
    }
    return ""
}


func (this *AllOne) GetMinKey() string {
    if this.head != nil {
        return this.head.name
    }
    return ""
}


/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */

var p = fmt.Println

func main() {
    a := Constructor()
    a.Inc("H")
    a.Inc("W")
    a.Inc("L")
    a.Inc("C")
    a.Inc("D")
    a.Inc("L")
    p(a.GetMaxKey())
    a.Inc("D")
    a.Dec("L")
    p(a.GetMaxKey())
    a.Dec("D")
    a.Inc("H")
    p(a.GetMaxKey())
    a.Inc("H")
    a.Inc("H")
    a.Dec("W")
    a.Dec("L")
    a.Dec("C")
    a.Dec("D")
    p(a.GetMaxKey())
    for range 6 {
        a.Inc("N")
    }
    p(a.GetMaxKey())
    p(a.GetMinKey())
}
