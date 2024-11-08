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

        let mask: i32 = (1 << maximum_bit) - 1;
        return prefix
            .into_iter()
            .rev()
            .map(|n| {
                n ^ mask
            })
            .collect();
    }
}


fn main() {
    let nums = [0,1,1,3];
    let maximum_bit: i32 = 2;

    let nums: Vec<i32> = nums.into();
    let res: Vec<i32> = Solution::get_maximum_xor(nums, maximum_bit);
    println!("{:?}", res);
}
