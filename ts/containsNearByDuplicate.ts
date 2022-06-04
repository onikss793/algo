function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const numsMap = new Map<number, number[]>();

  for (let currIdx = 0; currIdx < nums.length; currIdx++) {
    const num = nums[currIdx];

    if (!numsMap.get(num)?.length) {
      numsMap.set(num, [currIdx]);
      continue;
    }

    const indexes = numsMap.get(num) as number[];
    const lastIdx = indexes[indexes.length - 1];
    indexes.push(currIdx);

    if (Math.abs(currIdx - lastIdx) <= k) {
      return true;
    }
  }

  return false;
}

export default () => {
  const nums = [99, 99];
  const k = 2;
  // const nums = [1, 2, 3, 1, 2, 3];
  // const k = 2;
  // const nums = [1, 0, 1, 1];
  // const k = 1;
  // const nums = [1, 2, 3, 1];
  // const k = 3;
  const result = containsNearbyDuplicate(nums, k);
  console.log(result);
};
