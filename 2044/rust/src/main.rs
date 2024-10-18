struct Solution {}


impl Solution {
    pub fn count_max_or_subsets(nums: Vec<i32>) -> i32 {
        // get maximum bitwise or
        let max_or: i32 = nums.clone().into_iter().fold(0, |a, x| {a | x});

        return Self::count_subset(&nums, 0, 0, max_or);
    }

    fn count_subset(nums: &Vec<i32>, index: usize, curr_or: i32, target: i32) -> i32 {
        if index == nums.len() {
            if curr_or == target {
                return 1;
            } else {
                return 0;
            }
        }

        let with: i32 = Self::count_subset(nums, index + 1, curr_or, target);
        let without: i32 = Self::count_subset(nums, index + 1, curr_or | nums[index], target);

        return with + without;
    }
}


fn main() {
    let nums = [2,2,2];
    let nums: Vec<i32> = nums.to_vec();
    let res = Solution::count_max_or_subsets(nums);
    println!("{res}");
}
