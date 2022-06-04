fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut sorted = nums.clone();
    sorted.sort();

    let mut answer: Vec<Vec<i32>> = vec![];

    for (i, num) in sorted.clone().into_iter().enumerate() {
        if 0 < num {
            break;
        }
        if 0 < i && num == sorted[i - 1] {
            continue;
        }

        let mut j = i + 1;
        let mut k = sorted.len() - 1;

        while j < k {
            let sum = num + sorted[j] + sorted[k];

            if 0 < sum {
                k -= 1;
            } else if sum < 0 {
                j += 1;
            } else {
                answer.push(vec![num, sorted[j], sorted[k]]);
                j += 1;
                k -= 1;

                while sorted[j] == sorted[j - 1] && j < k {
                    j += 1;
                }
            }
        }
    }

    return answer;
}

pub fn main() {
    // let nums = vec![-1, 0, 1, 2, -1, -4];
    let nums = vec![
        8, 5, 12, 3, -2, -13, -8, -9, -8, 10, -10, -10, -14, -5, -1, -8, -7, -12, 4, 4, 10, -8, 0,
        -3, 4, 11, -9, -2, -7, -2, 3, -14, -12, 1, -4, -6, 3, 3, 0, 2, -9, -2, 7, -8, 0, 14, -1, 8,
        -13, 10, -11, 4, -13, -4, -14, -1, -8, -7, 12, -8, 6, 0, -15, 2, 8, -4, 11, -4, -15, -12,
        5, -9, 1, -2, -10, -14, -11, 4, 1, 13, -1, -3, 3, -7, 9, -4, 7, 8, 4, 4, 8, -12, 12, 8, 5,
        5, 12, -7, 9, 4, -12, -1, 2, 5, 4, 7, -2, 8, -12, -15, -1, 2, -11,
    ];
    let result = three_sum(nums);

    println!("result: {:?}", result);
}
