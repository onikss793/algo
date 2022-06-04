function convert(s: string, numRows: number): string {
  if (numRows === 1) return s;

  const arr: string[][] = Array.from({ length: numRows }, () => []);
  let opr: '+' | '-' = '+';
  let position = 0;

  for (let i = 0; i < s.length; i++) {
    console.log({ arr, position });
    const letter = s[i];
    arr[position].push(letter);

    if (position === 0) {
      position += 1;
      opr = '+';
      continue;
    }
    if (position === numRows - 1) {
      position -= 1;
      opr = '-';
      continue;
    }

    if (opr === '+') position += 1;
    if (opr === '-') position -= 1;
  }

  return arr.flat().join('');
}

export default () => {
  const s = 'PAYPALISHIRING';
  const numRows = 3;

  const result = convert(s, numRows);
  console.log(result);
};
