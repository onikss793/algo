function isSubsequence(s: string, t: string): boolean {
  if (!s.length) return true;

  let i = 0;
  let j = 0;

  while (i < s.length && j < t.length) {
    if (s[i] === t[j]) {
      i += 1;
      j += 1;

      if (i >= s.length) return true;
      continue;
    }

    j += 1;
  }

  return false;
}

export default () => {
  const s = 'abc';
  const t = 'ahbgdc';
  // const s = 'axc';
  // const t = 'ahbgdc';

  const result = isSubsequence(s, t);
  console.log(result);
};
