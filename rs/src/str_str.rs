fn str_str(haystack: String, needle: String) -> i32 {
    let matched = haystack.match_indices(&needle).into_iter().nth(0);
    match matched {
        Some((usize, _)) => usize as i32,
        None => -1,
    }
}

pub fn main() {
    let haystack = "leetcode".to_string();
    let needle = "leeto".to_string();

    let result = str_str(haystack, needle);

    println!("{result}");
}
