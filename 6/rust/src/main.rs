struct Solution {}


impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows as usize > s.len() {
            return s;
        }
        let mut res: Vec<Vec<char>> = Vec::with_capacity(num_rows as usize);
        for _ in 0..num_rows {
            res.push(Vec::new());
        }

        let mut dir: i32 = 1;
        let mut curr: i32 = 0;
        for c in s.chars() {
            res[curr as usize].push(c);
            if curr == num_rows - 1 {
                dir = -1;
            } else if curr == 0 {
                dir = 1;
            }
            curr += dir;
        }

        return res.into_iter().flatten().collect();
    }
}


fn main() {
    let s: &str = "PAYPALISHIRING";
    let num_rows: i32 = 3;
    let s: String = String::from(s);
    let res = Solution::convert(s, num_rows);
    println!("{res}");
}
