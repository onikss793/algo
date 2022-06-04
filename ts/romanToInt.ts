function romanToInt(s: string): number {
  let result = 0;
  const numMap = new Map([
    ['I', 1],
    ['V', 5],
    ['X', 10],
    ['L', 50],
    ['C', 100],
    ['D', 500],
    ['M', 1000],
  ]);

  let i = s.length - 1;

  while (i >= 0) {
    const number = numMap.get(s[i]);
    const num2 = numMap.get(s[i - 1]);

    if (!number) {
      break;
    }

    if (i === 0) {
      result += number;
      console.log({ i, result, number, num2 });
      break;
    }

    if (!num2) {
      break;
    }

    if (number <= num2) {
      result += number;
      console.log({ i, result, number, num2 });
      i -= 1;
      continue;
    }

    if (number > num2) {
      result += number - num2;
      console.log({ i, result, number, num2 });
      i -= 2;
      continue;
    }
  }

  return result;
}

export default () => {
  const s = 'LVIII';
  const result = romanToInt(s);
  console.log(result);
};
