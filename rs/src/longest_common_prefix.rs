fn longest_common_prefix(strs: Vec<String>) -> String {
    let mut sorted = strs.to_vec();
    sorted.sort_by(|a, b| a.len().cmp(&b.len()));

    let first = &sorted[0];
    println!("{:?}", sorted);

    let mut cache = "";

    for i in 0..first.len() {
        let prefix = &first[0..i + 1];
        let is_same = sorted.iter().all(|x| &x[0..i + 1] == prefix);

        if is_same {
            cache = prefix;
        } else {
            return cache.to_string();
        }
    }

    return cache.to_string();
}

pub fn main() {
    let strs: Vec<String> = vec![String::from("ab"), String::from("a")];
    let result = longest_common_prefix(strs);
    println!("{result}");
}
