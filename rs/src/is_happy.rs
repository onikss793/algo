use std::collections::HashMap;

fn is_happy(mut n: i32) -> bool {
    let mut seen: HashMap<i32, bool> = HashMap::new();

    while n != 1 && !seen.contains_key(&n) {
        seen.insert(n, true);
        n = get_next_number(n);
    }

    return n.eq(&1);
}

fn get_next_number(n: i32) -> i32 {
    let chars = n.to_string().chars().collect::<Vec<char>>();

    return chars.iter().fold(0, |acc, cur| {
        return acc + cur.to_digit(10).unwrap().pow(2) as i32;
    });
}

pub fn main() {
    let n: i32 = 19;
    let result = is_happy(n);

    println!("{result}");
}
