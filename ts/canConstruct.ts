function canConstruct(ransomNote: string, magazine: string): boolean {
  const arr: (string | null)[] = Array.from(magazine);

  for (const char of ransomNote) {
    const idx = arr.findIndex(it => it === char);
    if (idx === -1) return false;

    arr[idx] = null;
  }

  return true;
}

export default () => {
  const ransomNote = 'a';
  const magazine = 'b';
  // const ransomNote = 'aa';
  // const magazine = 'aab';

  const result = canConstruct(ransomNote, magazine);
  console.log(result);
};
