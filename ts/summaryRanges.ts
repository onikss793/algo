function summaryRanges(nums: number[]): string[] {
  const result: string[] = [];
  const arrow = '->';
  let cache = nums[0];
  let string = `${cache}`;

  for (let i = 1; i <= nums.length; i++) {
    const num = nums[i];

    if (num === cache + 1) {
      cache = num;
    } else {
      if (string !== String(cache)) {
        string += arrow;
        string += cache;
      }
      result.push(string);

      cache = num;
      string = `${num}`;
    }
  }

  return result;
}

export default () => {
  // const nums = [0, 2, 3, 4, 6, 8, 9];
  const nums = [0, 1, 2, 4, 5, 7];
  console.log(summaryRanges(nums));
};
