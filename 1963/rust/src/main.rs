struct Solution {}


impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let mut stack_size: i32 = 0;
        
        for c in s.chars() {
            if c == '[' {
                stack_size += 1;
            } else {
                if stack_size > 0 {
                    stack_size -= 1;
                }
            }
        }

        (stack_size + 1) / 2
    }
}


fn main() {
    let s: String = String::from("]]][[[");
    let res = Solution::min_swaps(s);
    println!("{res}");
}
