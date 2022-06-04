use std::collections::HashMap;

fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
    let mut map: HashMap<i32, Vec<i32>> = HashMap::new();

    for cur_idx in 0..nums.len() {
        let num = nums[cur_idx];

        if !map.contains_key(&num) {
            map.insert(num, [cur_idx as i32].to_vec());
            continue;
        }

        let indexes = map.get_mut(&num).unwrap();
        let last_idx = indexes.last().unwrap().to_owned();

        indexes.push(cur_idx as i32);

        if (cur_idx as i32) - last_idx <= k {
            return true;
        }
    }

    return false;
}

pub fn main() {
    let nums = vec![1, 2, 3, 1, 2, 3];
    let k = 2;
    // let nums = vec![1, 2, 3, 1];
    // let k = 3;

    let result = contains_nearby_duplicate(nums, k);
    println!("{result}");
}
