function canJump(nums: number[]): boolean {
  let target = nums.length - 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (i + nums[i] >= target) {
      target = i;
    }
  }

  return target === 0;
}

export default () => {
  // const nums = [2, 3, 1, 1, 4];
  // const nums = [2, 0];
  // const nums = [0, 2, 3];
  const nums = [0];
  const result = canJump(nums);

  console.log(result);
};
