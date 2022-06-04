use std::collections::HashMap;

fn length_of_longest_substring(s: String) -> i32 {
    let mut max_length = 0;
    let mut start = 0;
    let mut char_indices = HashMap::new();

    for (end, char) in s.chars().enumerate() {
        if let Some(&index) = char_indices.get(&char) {
            start = start.max(index + 1);
        }
        max_length = max_length.max(end - start + 1);
        char_indices.insert(char, end);
    }

    return max_length as i32;
}

pub fn main() {
    let s: String = "abcabcbb".to_string();
    let result = length_of_longest_substring(s);
    println!("{result}");
}
