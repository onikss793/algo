use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();
    let mut result: Vec<i32> = vec![];

    for (i, &n) in nums.iter().enumerate() {
        let diff = target - n;

        if let Some(&val) = map.get(&diff) {
            result.push(val);
            result.push(i as i32);

            break;
        } else {
            map.insert(n, i as i32);
        }
    }

    return result;
}

pub fn main() {
    let nums = vec![2, 7, 11, 15];
    let target: i32 = 9;

    let result = two_sum(nums, target);
    println!("{:?}", result);
}
