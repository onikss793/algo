fn reverse_words(s: String) -> String {
    return s.split_whitespace().rev().collect::<Vec<&str>>().join(" ");
}

pub fn main() {
    // let s: String = "a good example".to_string();
    let s: String = "the sky is blue".to_string();
    let result = reverse_words(s);

    println!("{result}");
}
