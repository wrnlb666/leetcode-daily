struct Solution {}


impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut shortest: usize = 200;
        for s in &strs {
            shortest = if shortest < String::len(&s) {shortest} else {String::len(&s)};
        }
        let mut res: Vec<u8> = vec!();
        'outer: for i in 0..shortest {
            let curr = strs[0].as_bytes()[i];
            for s in 1..strs.len() {
                if strs[s].as_bytes()[i] != curr {
                    break 'outer;
                }
            }
            res.push(curr);
        }
        String::from_utf8(res).unwrap()
    }
}


fn main() {
    let strs = ["flower","flow","flight"];
    let strs: Vec<String> = strs.into_iter().map(|s| {s.to_string()}).collect();
    let res: String = Solution::longest_common_prefix(strs);
    println!("{res}");
}
