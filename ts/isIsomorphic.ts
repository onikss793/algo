function isIsomorphic(s: string, t: string): boolean {
  const sMap = new Map<string, string>();
  const tMap = new Map<string, string>();

  for (let i = 0; i < s.length; i++) {
    const sEl = sMap.get(s[i]);
    const tEl = tMap.get(t[i]);

    if (!sEl && !tEl) {
      sMap.set(s[i], t[i]);
      tMap.set(t[i], s[i]);
      continue;
    }

    if (sEl !== t[i] || tEl !== s[i]) {
      return false;
    }
  }

  return true;
}

export default () => {
  // const s = 'badc';
  // const t = 'baba';
  // const s = 'foo';
  // const t = 'bar';
  // const s = 'paper';
  // const t = 'title';
  const s = 'egg';
  const t = 'add';

  const result = isIsomorphic(s, t);
  console.log(result);
};
