function isHappy(n: number): boolean {
  const nMap = new Map<number, boolean>();

  while (n !== 1 && !nMap.has(n)) {
    nMap.set(n, true);
    n = getNextNumber(n);
  }

  return n === 1;
}

function getNextNumber(n: number): number {
  const nextNumber = String(n)
    .split('')
    .reduce((a, b) => {
      return a + Math.pow(Number(b), 2);
    }, 0);

  console.log({ nextNumber });

  return nextNumber;
}

export default () => {
  const n = 2;
  console.log(isHappy(n));
};
