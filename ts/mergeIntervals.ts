function mergeIntervals(intervals: number[][]): number[][] {
  intervals.sort((a, b) => a[0] - b[0]);
  const result: number[][] = [];
  const first = intervals.at(0) as number[];
  let min: number = first[0];
  let max: number = first[1];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    if (max < start) {
      result.push([min, max]);

      min = start;
      max = end;
    } else {
      min = Math.min(min, start);
      max = Math.max(max, end);
    }
  }

  result.push([min, max]);

  return result;
}

export default () => {
  const intervals = [
    [1, 4],
    [0, 0],
  ];
  // const intervals = [
  //   [1, 4],
  //   [0, 4],
  // ];
  // const intervals = [
  //   [1, 4],
  //   [4, 5],
  // ];
  // const intervals = [
  //   [1, 3],
  //   [2, 6],
  //   [8, 10],
  //   [15, 18],
  // ];
  const result = mergeIntervals(intervals);
  console.log(result);
};
