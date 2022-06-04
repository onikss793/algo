function groupAnagrams(strs: string[]): string[][] {
  const strMap = new Map<string, string[]>();

  for (const str of strs) {
    const sorted = str.split('').sort().join();

    if (strMap.has(sorted)) {
      strMap.get(sorted)?.push(str);
    } else {
      strMap.set(sorted, [str]);
    }
  }

  return Array.from(strMap.values());
}

export default () => {
  const strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];
  const result = groupAnagrams(strs);
  console.log(result);
};
