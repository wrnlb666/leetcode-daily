struct Solution {}


impl Solution {
    pub fn longest_diverse_string(mut a: i32, mut b: i32, mut c: i32) -> String {
        let mut res: Vec<u8> = Vec::with_capacity((a + b + c) as usize);

        let mut curr_a: i32 = 0;
        let mut curr_b: i32 = 0;
        let mut curr_c: i32 = 0;
        while a + b + c != 0 {
            if a >= b && a >= c && a > 0 {
                if curr_a < 2 {
                    res.push(b'a');
                    a -= 1;
                    curr_a += 1;
                    curr_b = 0;
                    curr_c = 0;
                } else {
                    if b >= c && b > 0 {
                        res.push(b'b');
                        b -= 1;
                        curr_a = 0;
                        curr_b = 1;
                    } else if c > 0 {
                        res.push(b'c');
                        c -= 1;
                        curr_a = 0;
                        curr_c = 1;
                    } else {
                        break;
                    }
                }
            } else if b >= a && b >= c && b > 0 {
                if curr_b < 2 {
                    res.push(b'b');
                    b -= 1;
                    curr_b += 1;
                    curr_a = 0;
                    curr_c = 0;
                } else {
                    if a >= c && a > 0 {
                        res.push(b'a');
                        a -= 1;
                        curr_b = 0;
                        curr_a = 1;
                    } else if c > 0{
                        res.push(b'c');
                        c -= 1;
                        curr_b = 0;
                        curr_c = 1;
                    } else {
                        break;
                    }
                }
            } else if c >= a && c >= b && c > 0{
                if curr_c < 2 {
                    res.push(b'c');
                    c -= 1;
                    curr_c += 1;
                    curr_a = 0;
                    curr_b = 0;
                } else {
                    if a >= b && a > 0 {
                        res.push(b'a');
                        a -= 1;
                        curr_c = 0;
                        curr_a = 1;
                    } else if b > 0 {
                        res.push(b'b');
                        b -= 1;
                        curr_c = 0;
                        curr_b = 1;
                    } else {
                        break
                    }
                }
            } else {
                break;
            }
        }
        
        String::from_utf8(res).unwrap()
    }
}


fn main() {
    let a: i32 = 1;
    let b: i32 = 1;
    let c: i32 = 7;

    let res: String = Solution::longest_diverse_string(a, b, c);
    println!("{res}");
}
