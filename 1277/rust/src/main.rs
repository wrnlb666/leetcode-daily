struct Solution {}


impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        let mut res: i32 = 0;
        let mut dp: Vec<Vec<i32>> = vec![vec![-1; matrix[0].len()]; matrix.len()];
        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                res += Self::solve(i, j, &matrix, &mut dp)
            }
        }
        return res;
    }


    fn solve(i: usize, j: usize, grid: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) -> i32 {
        if i >= grid.len() || j >= grid[0].len() {
            return 0;
        }
        if grid[i][j] == 0 {
            return 0;
        }
        if dp[i][j] != -1 {
            return dp[i][j];
        }
        let right: i32 = Self::solve(i, j + 1, grid, dp);
        let diagonal: i32 = Self::solve(i + 1, j + 1, grid, dp);
        let below: i32 = Self::solve(i + 1, j, grid, dp);
        dp[i][j] = 1 + 
            if right <= diagonal && right <= below {right} 
            else if diagonal <= right && diagonal <= below {diagonal} 
            else {below};

        return dp[i][j];
    }
}


fn main() {
    let matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]];
    let matrix: Vec<Vec<i32>> = matrix.into_iter().map(|x| {x.to_vec()}).collect();
    let res: i32 = Solution::count_squares(matrix);
    println!("{res}");
}
