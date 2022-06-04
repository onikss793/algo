function isValidSudoku(board: string[][]): boolean {
  const validSet = new Set();

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      const cell = board[i][j];
      if (cell === '.') continue;

      const row = `row${i}: ${cell}`;
      const col = `col${j}: ${cell}`;
      const quad = `quad${3 * Math.floor(i / 3) + Math.floor(j / 3)}: ${cell}`;

      if (validSet.has(row) || validSet.has(col) || validSet.has(quad))
        return false;

      validSet.add(row).add(col).add(quad);
    }
  }

  return true;
}

function getRows(idx: number) {
  const mod = Math.floor(idx / 3);
  const val = Number.isInteger(mod) ? mod * 3 : 0;
  return [val, val + 1, val + 2];
}
function getColumns(idx: number) {
  const mod = idx % 3;

  const val = Number.isInteger(mod) ? mod * 3 : 0;
  return [val, val + 1, val + 2];
}

function isValid(arr: string[]): boolean {
  const filtered = arr.filter(it => it !== '.');
  return filtered.length === new Set(filtered).size;
}

export default () => {
  // const board = [
  //   ['.', '.', '.', '.', '5', '.', '.', '1', '.'],
  //   ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
  //   ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
  //   ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
  //   ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
  //   ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
  //   ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
  //   ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
  //   ['.', '.', '4', '.', '.', '.', '.', '.', '.'],
  // ];
  // false
  // const board = [
  //   ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
  //   ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  //   ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  //   ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  //   ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  //   ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  //   ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  //   ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  //   ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
  // ];
  // false
  const board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
  ];
  // true
  const result = isValidSudoku(board);
  console.log(result);
};
