function maxArea(height: number[]): number {
  let i = 0;
  let j = height.length - 1;
  let max = 0;

  while (i < j) {
    const ih = height[i];
    const jh = height[j];
    const contain = Math.min(ih, jh) * (j - i);
    max = Math.max(max, contain);

    if (ih <= jh) {
      i += 1;
    } else {
      j -= 1;
    }
  }

  return max;
}

export default () => {
  const height = [1, 2, 3, 4, 5, 25, 24, 3, 4];
  // const height = [1, 3, 2, 5, 25, 24, 5];
  // const height = [1, 1];
  // const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
  const result = maxArea(height);
  console.log(result);
};
