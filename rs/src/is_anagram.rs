use std::collections::HashMap;

fn is_anagram(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut s_map = s.chars().fold(HashMap::new(), |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        return acc;
    });

    return t.chars().all(|x| {
        if let Some(count) = s_map.get_mut(&x) {
            if *count == 0 {
                return false;
            }
            *count -= 1;
            return true;
        } else {
            return false;
        }
    });
}

pub fn main() {
    let s = "anagram".to_string();
    let t = "nagaram".to_string();

    let result = is_anagram(s, t);
    println!("{}", result);
}
