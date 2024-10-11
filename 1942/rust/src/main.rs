struct Solution {}


impl Solution {
    pub fn smallest_chair(mut times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        let target: Vec<i32> = times[target_friend as usize].clone();
        times.sort_by(|a, b| {a[0].cmp(&b[0])});

        let n: usize = times.len();
        let mut chair_time: Vec<i32> = vec![0; n];

        for time in times {
            for i in 0..n {
                if chair_time[i] <= time[0] {
                    chair_time[i] = time[1];
                    if time == target {
                        return i as i32;
                    }
                    break;
                }
            }
        }

        return 0;
    }
}


fn main() {
    let times = [[1,4],[2,3],[4,6]];
    let times: Vec<Vec<i32>> = times.map(|a| {a.to_vec()}).to_vec();
    let target_friend: i32 = 1;
    let res: i32 = Solution::smallest_chair(times, target_friend);
    println!("{res}");
}
