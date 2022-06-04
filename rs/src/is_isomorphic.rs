use std::collections::{HashMap, HashSet};

fn is_isomorphic(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut s_map: HashMap<char, char> = HashMap::new();
    let mut t_set: HashSet<char> = HashSet::new();

    for (s_char, t_char) in s.chars().zip(t.chars()) {
        if let Some(&mapped_char) = s_map.get(&s_char) {
            if mapped_char != t_char {
                return false;
            }
        } else {
            if t_set.contains(&t_char) {
                return false;
            }

            s_map.insert(s_char, t_char);
            t_set.insert(t_char);
        }
    }

    return true;
}

pub fn main() {
    let s = "egg".to_string();
    let t = "add".to_string();

    let result = is_isomorphic(s, t);
    println!("{}", result);
}
