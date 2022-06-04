function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sMap = new Map<string, number>();

  for (const char of s) {
    sMap.has(char)
      ? sMap.set(char, (sMap.get(char) as number) + 1)
      : sMap.set(char, 1);
  }

  for (const char of t) {
    const count = sMap.get(char);
    if (!count || count <= 0) return false;

    sMap.set(char, count - 1);
  }

  return true;
}

export default () => {
  const s = 'rat';
  const t = 'car';
  // const s = 'anagram';
  // const t = 'nagaram';
  const result = isAnagram(s, t);
  console.log(result);
};
