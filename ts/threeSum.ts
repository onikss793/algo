function twoSums(nums: number[], i: number, res: number[][]) {
  const seen = new Set();
  let j = i + 1;

  while (j < nums.length) {
    const complement = -nums[i] - nums[j];

    if (seen.has(complement)) {
      res.push([nums[i], nums[j], complement]);

      while (j + 1 < nums.length && nums[j] === nums[j + 1]) {
        j += 1;
      }
    }

    seen.add(nums[j]);
    j += 1;
  }
}

function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const answer: number[][] = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;
    if (nums[i] === nums[i - 1]) continue;

    let j = i + 1;
    let k = nums.length - 1;

    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k];
      console.log({ [i]: nums[i], [j]: nums[j], [k]: nums[k] });
      if (0 < sum) {
        k -= 1;
      } else if (sum < 0) {
        j += 1;
      } else {
        answer.push([nums[i], nums[j], nums[k]]);
        j += 1;
        k -= 1;

        while (nums[j] === nums[j - 1] && j < k) {
          j += 1;
        }
      }
    }
  }

  return answer;
}

export default () => {
  // const nums = [-1, 0, 1, 2, -1, -4];
  const nums = [
    8, 5, 12, 3, -2, -13, -8, -9, -8, 10, -10, -10, -14, -5, -1, -8, -7, -12, 4,
    4, 10, -8, 0, -3, 4, 11, -9, -2, -7, -2, 3, -14, -12, 1, -4, -6, 3, 3, 0, 2,
    -9, -2, 7, -8, 0, 14, -1, 8, -13, 10, -11, 4, -13, -4, -14, -1, -8, -7, 12,
    -8, 6, 0, -15, 2, 8, -4, 11, -4, -15, -12, 5, -9, 1, -2, -10, -14, -11, 4,
    1, 13, -1, -3, 3, -7, 9, -4, 7, 8, 4, 4, 8, -12, 12, 8, 5, 5, 12, -7, 9, 4,
    -12, -1, 2, 5, 4, 7, -2, 8, -12, -15, -1, 2, -11,
  ];
  const result = threeSum(nums);
  console.log(result);
};
