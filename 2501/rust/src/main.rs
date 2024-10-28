struct Solution {}


use std::collections::HashSet;


impl Solution {
    pub fn longest_square_streak(nums: Vec<i32>) -> i32 {
        let nums: HashSet<i64> = nums.into_iter().map(|x| {x as i64}).collect();
        let mut res: i32 = -1;
        for n in &nums {
            let mut n = *n;
            let mut i = 1;
            for _ in 0..5 {
                n *= n;
                if nums.contains(&n) {
                    i += 1;
                } else {
                    break;
                }
            }
            res = if i >= 2 && i >= res {i} else {res};
        }

        return res;
    }
}


fn main() {
    let nums = [4,3,6,16,8,2];
    let nums: Vec<i32> = nums.into();
    let res: i32 = Solution::longest_square_streak(nums);
    println!("{res}");
}
