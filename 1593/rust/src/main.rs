struct Solution {}


use std::cmp;
use std::collections::HashSet;


impl Solution {
    pub fn max_unique_split(s: String) -> i32 {
        let mut cache: HashSet<&str> = HashSet::new();
        return Self::rec(&mut cache, &s, 0);
    }

    
    fn rec<'a>(cache: &mut HashSet<&'a str>, s: &'a str, start: usize) -> i32 {
        if start == s.len() {
            return 0;
        }

        let mut count = 0;
        for end in (start + 1) .. (s.len() + 1) {
            let sub: &str = &s[start..end];
            if !cache.contains(sub) {
                cache.insert(sub);
                count = cmp::max(count, 1 + Self::rec(cache, s, end));
                cache.remove(sub);
            }
        }

        return count;
    }
}


fn main() {
    let s: &str = "ababccc";
    let s: String = String::from(s);
    let res: i32 = Solution::max_unique_split(s);
    println!("{res}");
}
