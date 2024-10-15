struct Solution {}


impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        let mut ones: i64 = 0;
        let mut res: i64 = 0;

        for c in s.chars() {
            if c == '1' {
                ones += 1;
            } else {
                res += ones
            }
        }

        return res;
    }
}


fn main() {
    let s: &str = "101";
    let s: String = String::from(s);
    let res: i64 = Solution::minimum_steps(s);
    println!("{res}");
}
