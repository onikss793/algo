fn form_range(min: i64, max: i64) -> String {
    let arrow: String = "->".to_string();

    if min == max {
        return min.to_string();
    }

    return min.to_string() + &arrow + &max.to_string();
}

fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
    if nums.len() == 0 {
        return vec![];
    }

    let mut result: Vec<String> = vec![];
    let mut min: i64 = nums[0] as i64;
    let mut max: i64 = nums[0] as i64;

    for &num in nums.iter().skip(1) {
        let num_64 = num as i64;

        if num_64 - max != 1 {
            result.push(form_range(min, max));
            min = num_64;
        }

        max = num_64;
    }
    result.push(form_range(min, max));

    return result;
}

pub fn main() {
    let nums: Vec<i32> = vec![-2147483648, -2147483647, 2147483647];
    // let nums: Vec<i32> = vec![0, 1, 2, 4, 5, 7];
    let result = summary_ranges(nums);
    println!("{:?}", result);
}
