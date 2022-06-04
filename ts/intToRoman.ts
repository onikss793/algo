const values = new Map([
  [1, 'I'],
  [4, 'IV'],
  [5, 'V'],
  [9, 'IX'],
  [10, 'X'],
  [40, 'XL'],
  [50, 'L'],
  [90, 'XC'],
  [100, 'C'],
  [400, 'CD'],
  [500, 'D'],
  [900, 'CM'],
  [1000, 'M'],
]);

function intToRoman(num: number): string {
  let result = '';
  const keys = Array.from(values.keys()).reverse();

  keys.forEach(key => {
    const quotient = Math.floor(num / key);
    if (quotient < 1) return;

    result += convertToRoman(values.get(key) as string, quotient);
    num -= key * quotient;

    console.log({
      key,
      num,
      result,
      convertToRoman: convertToRoman(values.get(key) as string, quotient),
    });
  });

  return result;
}

function convertToRoman(val: string, count: number) {
  let result = '';
  while (count > 0) {
    result += val;
    count -= 1;
  }

  return result;
}

export default () => {
  const num = 1994;

  const result = intToRoman(num);
  console.log(result);
};
