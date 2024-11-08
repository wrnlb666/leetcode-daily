struct Solution {}


impl Solution {
    pub fn get_maximum_xor(nums: Vec<i32>, maximum_bit: i32) -> Vec<i32> {
        let prefix: Vec<i32> = nums
            .into_iter()
            .scan(0, |curr, n| {
                *curr ^= n;
                Some(*curr)
            })
            .collect();

        prefix
            .into_iter()
            .rev()
            .map(|n| {
                Self::get_num(n, maximum_bit)
            })
            .collect()
    }

    fn get_num(n: i32, b: i32) -> i32 {
        let mut res: i32 = 0;
        for i in 0..b {
            if (n & (1 << i)) == 0 {
                res |= 1 << i;
            }
        }
        return res;
    }
}


fn main() {
    let nums = [0,1,1,3];
    let maximum_bit: i32 = 2;

    let nums: Vec<i32> = nums.into();
    let res: Vec<i32> = Solution::get_maximum_xor(nums, maximum_bit);
    println!("{:?}", res);
}
