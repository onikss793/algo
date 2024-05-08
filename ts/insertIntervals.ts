function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];
  const arr = intervals.concat([newInterval]);
  arr.sort((a, b) => a[0] - b[0]);

  const first = arr.at(0) as number[];
  let min: number = first[0];
  let max: number = first[1];

  for (let i = 1; i < arr.length; i++) {
    const [start, end] = arr[i];

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
    [1, 3],
    [6, 9],
  ];
  const newInterval = [2, 5];

  const result = insert(intervals, newInterval);
  console.log(result);
};
