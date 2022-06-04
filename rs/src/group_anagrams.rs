use std::collections::HashMap;

fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut str_map: HashMap<String, Vec<String>> = HashMap::new();

    for str in strs.iter() {
        let mut chars: Vec<char> = str.chars().collect();
        chars.sort_unstable();
        let sorted_str: String = chars.into_iter().collect();

        str_map
            .entry(sorted_str)
            .or_insert_with(Vec::new)
            .push(str.to_string());
    }

    return str_map.into_values().collect();
}

pub fn main() {
    let strs = [
        "eat".to_string(),
        "tea".to_string(),
        "tan".to_string(),
        "ate".to_string(),
        "nat".to_string(),
        "bat".to_string(),
    ]
    .to_vec();
    let result = group_anagrams(strs);

    println!("{:?}", result);
}
