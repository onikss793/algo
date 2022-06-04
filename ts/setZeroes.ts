/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  const x: number[] = [];
  const y: number[] = [];

  matrix.forEach((row, i) => {
    row.forEach((col, j) => {
      if (col === 0) {
        x.push(i);
        y.push(j);
      }
    });
  });

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (x.includes(i) || y.includes(j)) {
        matrix[i][j] = 0;
      }
    }
  }
}

export default () => {
  const matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
  ];
  setZeroes(matrix);
  console.log(matrix);
};
