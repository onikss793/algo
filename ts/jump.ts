function jump(nums: number[]): number {
  let answer = 0;
  let currEnd = 0;
  let currFar = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    currFar = Math.max(currFar, i + nums[i]);

    if (i === currEnd) {
      answer += 1;
      currEnd = currFar;
    }
  }

  return answer;
}

export default () => {
  const nums = [2, 3, 1, 1, 4];

  const result = jump(nums);
  console.log(result);
};
