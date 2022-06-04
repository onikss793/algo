function longestCommonPrefix(strs: string[]): string {
  const first = strs[0];
  let cache = '';

  for (let i = 0; i < first.length; i++) {
    const prefix = first.slice(0, i + 1);
    const isSame = strs.every(it => {
      const compare = it.slice(0, i + 1);
      return prefix === compare;
    });

    console.log({ prefix, isSame });

    if (isSame) cache = prefix;
    else return cache;
  }

  return cache;
}

export default () => {
  // const strs = ['flower', 'flow', 'flight'];
  // const strs = ['dog', 'racecar', 'car'];
  const strs = ['a'];
  const result = longestCommonPrefix(strs);

  console.log(result);
};
