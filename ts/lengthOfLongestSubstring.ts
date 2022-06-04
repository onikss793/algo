function lengthOfLongestSubstring(s: string): number {
  let i = 0;
  let j = 1;
  let maxLength = 0;
  const charSet = new Set();
  const str = s.replace(/ /g, '뷁');

  while (i < str.length) {
    if (i >= j) {
      j += 1;
      continue;
    }

    const chars = str.slice(i, j);
    console.log({ i, j, chars });

    if (j > str.length) {
      i += 1;
      j = i + 1;
      continue;
    }

    if (!charSet.has(chars)) {
      maxLength = Math.max(maxLength, chars.length);
      charSet.add(chars);
    }

    if (chars.includes(str[j])) {
      i += 1;
    } else {
      j += 1;
    }
  }

  console.log(charSet);
  return maxLength;
}

export default () => {
  const s = '   ';
  // const s = 'pwwkew';
  // const s = 'bbbbb';
  // const s = 'abcabcbb';
  const result = lengthOfLongestSubstring(s);
  console.log(result);
};
