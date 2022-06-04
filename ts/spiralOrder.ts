function spiralOrder(matrix: number[][]): number[] {
  if (matrix.length === 0) return [];
  const result: number[] = [];

  let top = 0;
  let bottom = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top += 1;

    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right -= 1;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom -= 1;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left += 1;
    }
  }

  return result;
}

export default () => {
  // const matrix = [
  //   [1, 2, 3, 4, 5],
  //   [6, 7, 8, 9, 10],
  //   [11, 12, 13, 14, 15],
  //   [16, 17, 18, 19, 20],
  //   [21, 22, 23, 24, 25],
  // ];
  const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  const result = spiralOrder(matrix);
  console.log(result);
};
