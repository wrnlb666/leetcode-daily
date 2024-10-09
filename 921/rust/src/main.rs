struct Solution {}


impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut right: i32 = 0;
        let mut left: i32 = 0;
        for c in s.chars() {
            if c == '(' {
                left += 1;
            } else if c == ')' {
                if left > 0 {
                    left -= 1
                } else {
                    right += 1
                }
            }
        }
        left + right
    }
}


fn main() {
    let s: &str = "(((";
    let s: String = s.to_string();
    let res: i32 = Solution::min_add_to_make_valid(s);
    println!("{res}");
}
