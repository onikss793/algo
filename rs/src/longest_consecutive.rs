use std::collections::HashSet;

fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let num_set: HashSet<i32> = nums.into_iter().collect();
    let mut longest_consecutive = 0;

    for &num in num_set.iter() {
        if num_set.contains(&(num - 1)) {
            continue;
        }

        let mut streak = 1;
        let mut consecutive = num;

        while num_set.contains(&(consecutive + 1)) {
            consecutive += 1;
            streak += 1;
        }

        longest_consecutive = longest_consecutive.max(streak);
    }

    return longest_consecutive;
}

pub fn main() {
    let nums = vec![100, 4, 200, 1, 3, 2];
    let result = longest_consecutive(nums);
    println!("Result: {}", result);
}
