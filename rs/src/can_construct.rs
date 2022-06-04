fn can_construct(ransom_note: String, magazine: String) -> bool {
    let ransom_note_chars: Vec<char> = ransom_note.chars().collect(); // Convert str to Vec<char>
    let mut magazine_mut = magazine.clone(); // Convert &str to String

    for ch in ransom_note_chars {
        match magazine_mut.find(ch) {
            Some(idx) => {
                magazine_mut.remove(idx);
            }
            None => {
                return false;
            }
        }
    }

    return true;
}

pub fn main() {
    let ransom_note = "aa".to_string();
    let magazine = "aab".to_string();

    let result = can_construct(ransom_note, magazine);
    println!("{}", result);
}
