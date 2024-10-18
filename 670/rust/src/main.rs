struct Solution {}


impl Solution {
    pub fn maximum_swap(mut num: i32) -> i32 {
        if num == 0 {
            return num
        }
        let mut elems: Vec<i32> = Vec::new();
        while num != 0 {
            elems.push(num % 10);
            num /= 10;
        }
        elems.reverse();
        let mut sorted: Vec<i32> = elems.clone();
        sorted.sort_by(|a, b| {b.cmp(a)});

        for i in 0..elems.len() {
            if elems[i] == sorted[i] {
                continue;
            }
            for j in (i..elems.len()).rev() {
                if elems[j] == sorted[i] {
                    elems[j] = elems[i];
                    elems[i] = sorted[i];
                }
            }
            break;
        }

        return elems.into_iter().fold(0, |c, v| {c * 10 + v})
    }
}


fn main() {
    let num: i32 = 1993;
    let res: i32 = Solution::maximum_swap(num);
    println!("{res}");
}
