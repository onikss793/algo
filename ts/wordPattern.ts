function wordPattern(pattern: string, s: string): boolean {
  const pMap = new Map<string, string>();
  const sMap = new Map<string, string>();
  const sArr = s.split(' ');

  if (pattern.length !== sArr.length) return false;

  for (let i = 0; i < pattern.length; i++) {
    const x = pattern[i];
    const y = sArr[i];

    if (pMap.has(x)) {
      if (pMap.get(x) !== y) return false;
    }

    if (sMap.has(y)) {
      if (sMap.get(y) !== x) return false;
    }

    pMap.set(x, y);
    sMap.set(y, x);
  }

  return true;
}

export default () => {
  const pattern = 'abba';
  const s = 'dog cat cat fish';
  // const pattern = 'abba';
  // const s = 'dog cat cat dog';

  const result = wordPattern(pattern, s);
  console.log(result);
};
