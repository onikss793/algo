function hIndex(citations: number[]): number {
  citations.sort((a, b) => a - b);
  let maximum = 0;

  if (citations.length === 1 && citations[0] !== 0) return 1;

  for (let i = 0; i < citations.length; i++) {
    const c = citations[i];
    if (c === 0) continue;

    const count = citations.length - i;
    const next = citations[i + 1];
    if (i + 1 === citations.length || next >= c) {
      const value = Math.min(count, c);
      maximum = Math.max(value, maximum);
    }
  }

  return maximum;
}

export default () => {
  // const citations = [3, 0, 6, 1, 5]; // [0, 1, 3, 5, 6]
  // const citations = [1, 3, 1];
  // const citations = [1];
  // const citations = [100];
  // const citations = [6, 6, 4, 8, 4, 3, 3, 10]; // [3, 3, 4, 6, 6, 8, 10]
  // const citations = [1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3];
  // const citations = [11, 15];
  const citations = [1, 2, 100];

  const result = hIndex(citations);
  console.log('result: ', result);
};
