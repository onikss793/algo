function twoSum(nums: number[], target: number): number[] {
  const result: number[] = [];
  const hashMap = new Map<number, number>(); // { value: index }

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];

    if (hashMap.has(diff)) {
      result.push(hashMap.get(diff) as number, i);
      break;
    }

    hashMap.set(nums[i], i);
  }

  return result;
}

export default () => {
  const nums = [-3, 4, 3, 90];
  const target = 0;
  // const nums = [0, 4, 3, 0];
  // const target = 0;
  // const nums = [3, 3];
  // const target = 6;
  // const nums = [3, 2, 4];
  // const target = 6;
  // const nums = [2, 7, 11, 15];
  // const target = 9;

  const result = twoSum(nums, target);
  console.log(result);
};
