function majorityElement(nums: number[]): number {
  const numMap = nums.reduce((acc, curr) => {
    acc.set(curr, !!acc.get(curr) ? Number(acc.get(curr)) + 1 : 1);

    return acc;
  }, new Map<number, number>());
  let largestKey = nums[0];

  // @ts-ignore
  for (const [key, value] of numMap.entries()) {
    if (value > Number(numMap.get(largestKey))) {
      largestKey = Number(key);
    }
  }

  console.log(largestKey);
  return largestKey;
}

export default () => {
  majorityElement([6, 5, 5]);
};
