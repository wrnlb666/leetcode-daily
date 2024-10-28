struct Solution {}


impl Solution {
    pub fn reverse(mut x: i32) -> i32 {
        if x == 0 {
            return 0;
        }
        let sign: i32 = if x >= 0 {1} else {x = -x; -1};
        let mut res: i64 = 0;
        while x > 0 {
            res *= 10;
            res += (x % 10) as i64;
            x /= 10;
        }

        if res < i32::min_value() as i64 || res > i32::max_value() as i64 {
            return 0
        }
        return res as i32 * sign;
    }
}


fn main() {
    let x: i32 = 123;
    let res: i32 = Solution::reverse(x);
    println!("{res}");
}
