fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut i = 0;
    let mut j = numbers.len() - 1;
    let mut result = vec![1, 2];

    while i < j {
        let sum = numbers[i] + numbers[j];

        if sum == target {
            result[0] = i as i32 + 1;
            result[1] = j as i32 + 1;
            break;
        } else if sum < target {
            i += 1;
        } else {
            j -= 1;
        }
    }

    return result;
}

pub fn main() {
    let numbers = vec![2, 3, 4];
    let target = 6;

    let result = two_sum(numbers, target);
    println!("{:?}", result);
}
