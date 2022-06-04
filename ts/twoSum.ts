function twoSum(numbers: number[], target: number): number[] {
  let i = 0;
  let j = numbers.length - 1;

  while (i < j) {
    const sum = numbers[i] + numbers[j];

    if (sum === target) {
      return [i + 1, j + 1];
    } else if (sum < target) {
      i += 1;
    } else {
      j -= 1;
    }
  }

  return [1, 2];
}

export default () => {
  // const numbers = [-1, 0];
  // const target = -1;
  const numbers = [2, 3, 4];
  const target = 6;
  // const numbers = [2, 7, 11, 15];
  // const target = 9;
  const result = twoSum(numbers, target);

  console.log(result);
};
