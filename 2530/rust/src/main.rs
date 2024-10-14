struct Solution {}


use std::collections::BinaryHeap;


impl Solution {
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        let mut heap: BinaryHeap<i32> = BinaryHeap::new();
        nums.iter().for_each(|n| {heap.push(*n)});

        let mut res: i64 = 0;
        for _ in 0..k {
            let curr = heap.pop().unwrap();
            res += curr as i64;
            heap.push(if curr % 3 == 0 {curr / 3} else {curr / 3 + 1});
        }

        return res;
    }
}


fn main() {
    let nums = [1,10,3,3,3];
    let nums: Vec<i32> = nums.to_vec();
    let k: i32 = 3;
    let res: i64 = Solution::max_kelements(nums, k);
    println!("{res}");
}
