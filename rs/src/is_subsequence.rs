fn is_subsequence(s: String, t: String) -> bool {
    let s_chars: Vec<_> = s.chars().collect();
    let t_chars: Vec<_> = t.chars().collect();

    if s_chars.is_empty() {
        return true;
    } else if t_chars.is_empty() {
        return false;
    }

    let mut i = 0 as usize;
    let mut j = 0 as usize;

    while i < s_chars.len() && j < t_chars.len() {
        if s_chars.iter().nth(i) == t_chars.iter().nth(j) {
            i += 1;
            j += 1;

            if i >= s.len() {
                return true;
            }

            continue;
        }

        j += 1;
    }

    return false;
}

pub fn main() {
    let s = "abc".to_string();
    let t = "ahbgdc".to_string();

    let result = is_subsequence(s, t);
    println!("{result}");
}
