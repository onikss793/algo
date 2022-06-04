fn convert(s: String, num_rows: i32) -> String {
    if num_rows == 1 {
        return s;
    }

    let mut arr = vec![Vec::<char>::new(); num_rows as usize];
    let mut opr = '+';
    let mut position = 0;

    for i in 0..s.len() {
        let letter = s.chars().nth(i).unwrap();
        arr[position].push(letter);

        if position == 0 {
            position += 1;
            opr = '+';
            continue;
        }
        if position == (num_rows - 1) as usize {
            position -= 1;
            opr = '-';
            continue;
        }

        if opr == '+' {
            position += 1;
        }
        if opr == '-' {
            position -= 1;
        }
    }

    return arr.iter().flatten().collect();
}

pub fn main() {
    let s = "PAYPALISHIRING".to_string();
    let num_rows = 3;

    let result = convert(s, num_rows);
    println!("{result}");
}
