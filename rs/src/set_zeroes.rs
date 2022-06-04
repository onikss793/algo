fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
    let mut x: Vec<usize> = vec![];
    let mut y: Vec<usize> = vec![];

    for (i, row) in matrix.iter().enumerate() {
        for (j, col) in row.iter().enumerate() {
            if col.to_owned() == 0 {
                x.push(i);
                y.push(j);
            }
        }
    }

    for i in 0..matrix.len() {
        for j in 0..matrix[i].len() {
            if x.contains(&i) || y.contains(&j) {
                matrix[i][j] = 0;
            }
        }
    }
}

pub fn main() {
    let mut matrix = [vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]].to_vec();
    set_zeroes(&mut matrix);
    println!("{:?}", matrix);
}
