struct Solution {}


impl Solution {
    pub fn remove_subfolders(mut folder: Vec<String>) -> Vec<String> {
        folder.sort();

        let mut res: Vec<String> = Vec::new();
        let mut curr: String = folder[0].to_owned() + "/";
        folder.iter().for_each(|s| {
            if !s.starts_with(&curr) {
                res.push(s.to_owned());
                curr = s.to_owned() + "/";
            }
        });

        return res;
    }
}


pub fn main() {
    let folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"];
    let folder: Vec<String> = folder.into_iter().map(|x| {String::from(x)}).collect();
    let res: Vec<String> = Solution::remove_subfolders(folder);
    println!("{res:?}");
}
