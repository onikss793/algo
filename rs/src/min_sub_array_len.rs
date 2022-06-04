fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
    const MAX: usize = usize::MAX;
    let mut min_length = MAX;
    let mut sum = 0;
    let mut left = 0;

    for right in 0..nums.len() {
        sum += nums[right];

        while sum >= target {
            min_length = min_length.min(right - left + 1);
            sum -= nums[left];
            left += 1;
        }
    }

    if min_length == MAX {
        return 0;
    } else {
        return min_length as i32;
    };
}

pub fn main() {
    let target = 11;
    let nums = vec![1, 2, 3, 4, 5];
    let result = min_sub_array_len(target, nums);
    println!("{result}");
}
