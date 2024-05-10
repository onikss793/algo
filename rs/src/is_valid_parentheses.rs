use std::collections::HashMap;

fn is_valid_parentheses(s: String) -> bool {
    let brackets = HashMap::from([(')', '('), ('}', '{'), (']', '[')]);
    let mut stack: Vec<char> = vec![];
    let openers = ['(', '{', '['];

    for bracket in s.chars().into_iter() {
        println!("stack: {:?} | bracket: {bracket}", stack);
        if openers.contains(&bracket) {
            stack.push(bracket);
        } else {
            match stack.pop() {
                Some(last) => {
                    let &matching = brackets.get(&bracket).unwrap();

                    println!("last: {last} | matching: {matching}");

                    if last != matching {
                        return false;
                    }
                }
                None => {
                    return false;
                }
            };
        }
    }

    return stack.len() == 0;
}

pub fn main() {
    let s: String = "()[]{}".to_string();
    // let s: String = "()".to_string();
    let result = is_valid_parentheses(s);

    println!("{result}");
}
