struct Solution {}


impl Solution {
    pub fn find_kth_bit(_n: i32, k: i32) -> char {
        if k == 1 {
            return '0';
        } else if k == 2 {
            return '1';
        } else if k == 3 {
            return '1';
        }

        let mut len: i32 = 1;
        while len < k {
            len = len * 2 + 1;
        }
        let mut res: Vec<bool> = Vec::with_capacity(len as usize);
        res.push(false);
        Self::foo(&mut res, len as usize);

        return if res[(k-1) as usize] {'1'} else {'0'};
    }


    fn foo(res: &mut Vec<bool>, len: usize) {
        if res.len() == len {
            return
        }
        res.push(true);
        for i in (0..res.len()-1).rev() {
            res.push(!res[i]);
        }
        Self::foo(res, len);
    }
}


fn main() {
    let n: i32 = 4;
    let k: i32 = 11;
    let res: char = Solution::find_kth_bit(n, k);
    println!("{res:?}");
}
