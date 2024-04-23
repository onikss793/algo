function longestConsecutive(nums: number[]): number {
  const set = new Set(nums);
  let longestConsecutive = 0;

  for (const num of set) {
    if (set.has(num - 1)) {
      continue;
    }

    let streak = 1;
    let consecutive = num;

    while (set.has(consecutive + 1)) {
      consecutive += 1;
      streak += 1;
    }

    longestConsecutive = Math.max(streak, longestConsecutive);
  }

  return longestConsecutive;
}

export default () => {
  const nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1];
  // const nums = [100, 4, 200, 1, 3, 2];
  console.log(longestConsecutive(nums));
};
