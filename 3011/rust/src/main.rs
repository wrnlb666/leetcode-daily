struct Solution {}


impl Solution {
    pub fn can_sort_array(nums: Vec<i32>) -> bool {
        let mut curr: (i32, i32) = (Self::icb(nums[0]), nums[0]);
        let mut last: i32 = i32::min_value();

        for &n in &nums[1..] {
            let bs: i32 = Self::icb(n);
            if bs == curr.0 {
                if n < last {
                    return false;
                }
                if n > curr.1 {
                    curr.1 = n;
                }
            } else {
                last = curr.1;
                if n < last {
                    return false;
                }
                curr = (bs, n);
            }
        }

        return true;
    }


    fn icb(n: i32) -> i32 {
        let mut res = 0;
        for i in 0..32 {
            if (n & (1 << i)) != 0 {
                res += 1;
            }
        }
        return res;
    }
}


fn main() {
    let nums = [8,4,2,30,15];
    let nums: Vec<i32> = nums.to_vec();
    let res: bool = Solution::can_sort_array(nums);
    println!("{res}");
}
