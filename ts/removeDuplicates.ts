export const removeDuplicates = (nums: number[]): number => {
  let count = 0;
  const newNums = nums.map((num, idx) => {
    const i = nums.findIndex(it => it === num);
    if (i !== idx) {
      return Infinity;
    }

    count += 1;
    return num;
  });

  newNums.sort((a, b) => a - b).forEach((num, idx) => (nums[idx] = num));

  return count;
};
