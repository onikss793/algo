function rotate(nums: number[], k: number): void {
  if (nums.length === 0) return;
  if (k === 0) return;

  const copy = nums.slice().reverse();

  const pre = copy.slice(0, k).reverse();
  const sub = copy.slice(k, nums.length).reverse();

  pre.concat(sub).forEach((num, idx) => (nums[idx] = num));
}

export default () => {
  // const nums = [1, 2];
  // const k = 0;

  // const nums = [-1];
  // const k = 2;

  // const nums = [-1, -100, 3, 99];
  // const k = 2;

  const nums = [1, 2, 3, 4, 5, 6, 7];
  const k = 3;

  rotate(nums, k);

  console.log(JSON.stringify(nums));
};
