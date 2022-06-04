// use regex::Regex;
// use std::cmp::Reverse;

fn is_palindrome(s: String) -> bool {
    if s.len() <= 1 {
        return true;
    }

    let binding = s.to_ascii_lowercase();
    let mut chars = binding.chars().filter(|x| x.is_ascii_alphanumeric());

    while let Some((front, back)) = chars.next().zip(chars.next_back()) {
        if front != back {
            return false;
        }
    }

    return true;
    //     let replaced = s
    //         .chars()
    //         .filter(|x| x.is_alphanumeric())
    //         .collect::<String>()
    //         .to_lowercase();
    //
    //     let mut i = 0 as usize;
    //     let mut j = replaced.len().wrapping_sub(1);
    //
    //     while i < j && j < replaced.len() {
    //         if replaced.chars().nth(i).unwrap() != replaced.chars().nth(j).unwrap() {
    //             return false;
    //         }
    //
    //         i += 1;
    //         j -= 1;
    //     }
    //
    //     return true;
}

// fn is_palindrome(s: String) -> bool {
//     let replaced = Regex::new(r"[^a-zA-Z0-9]")
//         .unwrap()
//         .replace_all(s.as_str(), "")
//         .to_lowercase();
//     let reversed = Reverse(&replaced).0.to_string();
//     println!("{replaced} {reversed}");
//
//     return replaced == reversed;
// }

pub fn main() {
    // let s: String = "A man, a plan, a canal: Panama".to_string();
    // let s: String = "race a car".to_string();
    let s: String = " ".to_string();
    let result = is_palindrome(s);

    println!("{result}");
}
