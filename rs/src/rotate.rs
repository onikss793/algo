fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let n = matrix.len();

    for i in 0..n {
        for j in i + 1..n {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    for row in matrix.iter_mut() {
        row.reverse();
    }
}

pub fn main() {
    let mut matrix: Vec<Vec<i32>> =
        [[1, 2, 3].to_vec(), [4, 5, 6].to_vec(), [7, 8, 9].to_vec()].to_vec();
    rotate(&mut matrix);
    println!("{:?}", matrix);
}
