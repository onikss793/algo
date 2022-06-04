fn max_area(height: Vec<i32>) -> i32 {
    let mut i = 0 as usize;
    let mut j = height.len() - 1;
    let mut max = 0;

    while i < j {
        let left = height[i];
        let right = height[j];
        let area = left.min(right) * (j - i) as i32;
        max = max.max(area);

        if left <= right {
            i += 1;
        } else {
            j -= 1;
        }
    }

    return max;
}

pub fn main() {
    let height = vec![1, 1];
    // let height = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];
    let result = max_area(height);
    println!("{result}");
}
