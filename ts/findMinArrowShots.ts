function findMinArrowShots(points: number[][]): number {
  if (points.length === 0) return 0;
  points.sort((a, b) => a[1] - b[1]);

  let count = 1;
  let [_, max] = points[0];

  for (let i = 1; i < points.length; i++) {
    const [start, end] = points[i];

    if (start <= max) {
      continue;
    }

    max = end;
    count += 1;
  }

  return count;
}

export default () => {
  const points = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
  ];
  // const points = [
  //   [1, 2],
  //   [3, 4],
  //   [5, 6],
  //   [7, 8],
  // ];
  // const points = [
  //   [10, 16],
  //   [2, 8],
  //   [1, 6],
  //   [7, 12],
  // ];
  const result = findMinArrowShots(points);
  console.log(result);
};
