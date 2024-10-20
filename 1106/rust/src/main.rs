struct  Solution {}


impl Solution {
    pub fn parse_bool_expr(expression: String) -> bool {
        let mut i: usize = 0;
        Self::parse(&expression.chars().collect(), &mut i)
    }


    fn parse(expr: &Vec<char>, i: &mut usize) -> bool {
        if expr[*i] == 't' {
            return true;
        } else if expr[*i] == 'f' {
            return false;
        }

        match expr[*i] {
            '!' => {
                *i += 2;
                let res = !Self::parse(expr, i);
                *i += 1;
                return res;
            },
            '&' => {
                *i += 2;
                while expr[*i] != ')' {
                    if expr[*i] != ',' {
                        if Self::parse(expr, i) == false {
                            Self::short_circut(expr, i);
                            return false;
                        }
                    }
                    *i += 1;
                }
                return true;
            },
            '|' => {
                *i += 2;
                while expr[*i] != ')' {
                    if expr[*i] != ',' {
                        if Self::parse(expr, i) == true {
                            Self::short_circut(expr, i);
                            return true;
                        }
                    }
                    *i += 1;
                }
                return false;
            },
            _   => {
                return false;
            }
        }
    }


    fn short_circut(expr: &Vec<char>, i: &mut usize) {
        let mut left: i32 = 1;
        loop {
            if expr[*i] == '(' {
                left += 1;
            } else if expr[*i] == ')' {
                left -= 1;
                if left == 0 {
                    return;
                }
            }
            *i += 1;
        }
    }
}


fn main() {
    let expression: &str = "&(&(&(!(&(f)),&(t),|(f,f,t)),|(t),|(f,f,t)),!(&(|(f,f,t),&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))),&(t))),&(!(&(&(!(&(f)),&(t),|(f,f,t)),|(t),|(f,f,t))),!(&(&(&(t,t,f),|(f,f,t),|(f)),!(&(t)),!(&(|(f,f,t),&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))),&(t))))),!(&(f))))";
    let expression: String = String::from(expression);
    let res: bool = Solution::parse_bool_expr(expression);
    println!("{res}");
}
