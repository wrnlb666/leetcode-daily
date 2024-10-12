struct Solution {}


impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut events: Vec<(i32, i32)> = Vec::with_capacity(intervals.len() * 2);

        for i in intervals {
            events.push((i[0], 1));
            events.push((i[1] + 1, -1));
        }

        events.sort_by(|a, b| {
            let temp: std::cmp::Ordering = a.0.cmp(&b.0);
            match temp {
                std::cmp::Ordering::Equal => a.1.cmp(&b.1),
                _ => temp
            }
        });
        //println!("{:?}", events);

        let mut res: i32 = 0;
        let mut curr: i32 = 0;

        for e in events {
            curr += e.1;
            res = if res > curr {res} else {curr};
        }

        return res;
    }
}


fn main() {
    let intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]];
    let intervals: Vec<Vec<i32>> = intervals.map(|interval| {interval.to_vec()}).to_vec();
    let res: i32 = Solution::min_groups(intervals);
    println!("{res}");
}
