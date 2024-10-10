struct Solution {}


impl Solution {
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();
        let mut right_max: Vec<i32> = nums.to_vec();

        for i in (0..(n-1)).rev() {
            right_max[i] = if right_max[i] > right_max[i+1] {right_max[i]} else {right_max[i+1]}
        }
        
        let mut left: usize = 0;
        let mut right: usize = 0;
        let mut max_width: usize = 0;

        while right < n {
            while (left < right) && (nums[left] > right_max[right]) {
                left += 1;
            }
            max_width = if max_width > (right - left) {max_width} else {right - left};
            right += 1;
        }

        max_width as i32
    }
}


fn main() {
    let nums: Vec<i32> = [9,8,1,0,1,9,4,0,4,1].to_vec();
    let res: i32 = Solution::max_width_ramp(nums);
    println!("{res}");
}
