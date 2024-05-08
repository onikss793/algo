fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
    if points.len() == 0 {
        return 0;
    }
    points.sort_by(|a, b| a[1].cmp(&b[1]));

    let mut count: i32 = 1;
    let mut max = points[0][1];

    for i in 1..points.len() {
        if points[i][0] <= max {
            continue;
        }

        max = points[i][1];
        count += 1;
    }

    return count;
}

pub fn main() {
    let points: Vec<Vec<i32>> = vec![vec![10, 16], vec![2, 8], vec![1, 6], vec![7, 12]];
    let result = find_min_arrow_shots(points);

    println!("{result}");
}
