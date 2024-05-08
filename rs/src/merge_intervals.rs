fn merge_intervals(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    intervals.sort();
    let mut result: Vec<Vec<i32>> = vec![];
    let first = &intervals[0];
    let mut min = first[0];
    let mut max = first[1];

    for interval in intervals.iter().skip(1) {
        let start = interval[0];
        let end = interval[1];

        if max < start {
            result.push(vec![min, max]);

            min = start;
            max = end;
        } else {
            min = min.min(start);
            max = max.max(end);
        }
    }

    result.push(vec![min, max]);

    return result;
}

pub fn main() {
    let intervals = vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]];

    let result = merge_intervals(intervals);
    println!("{:?}", result);
}
