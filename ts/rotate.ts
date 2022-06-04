/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j <= i; j++) {
      const a = matrix[i][j];
      const b = matrix[j][i];
      matrix[i][j] = b;
      matrix[j][i] = a;
    }

    matrix[i].reverse();
  }

  // for (let i = 0; i < matrix.length; i++) {
  //   matrix[i].reverse();
  // }
}

export default () => {
  const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  rotate(matrix);
  console.log(matrix);
};
