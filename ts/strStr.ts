function strStr(haystack: string, needle: string): number {
  const splitted = haystack.split(needle);
  return splitted.length === 1 ? -1 : splitted[0].length;

  // return haystack.indexOf(needle);

  //   for (let i = 0; i < haystack.length; i++) {
  //     const letter = haystack[i];
  //     if (letter !== needle[0]) continue;
  //
  //     if (Array.from(needle).every((n, idx) => n === haystack[i + idx])) {
  //       return i;
  //     }
  //   }
  //
  //   return -1;
}

export default () => {
  const haystack = 'leetcode';
  const needle = 'leeto';

  const result = strStr(haystack, needle);
  console.log(result);
};
