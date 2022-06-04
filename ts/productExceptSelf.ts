const productExceptSelf = (nums: number[]): number[] => {
  let cache = 1;
  const indexes = nums.map((_, idx) => idx);

  const left = indexes.map(idx => {
    return idx === 0 ? (cache = 1) : (cache = nums[idx - 1] * cache);
  });

  const right = indexes
    .reverse()
    .map(idx => {
      return idx === nums.length - 1
        ? (cache = 1)
        : (cache = nums[idx + 1] * cache);
    })
    .reverse();

  return nums.map((_, idx) => left[idx] * right[idx]);
};

export default () => {
  const nums = [4, 5, 1, 8, 2];
  const result = productExceptSelf(nums);
  console.log(result);
};
