function canCompleteCircuit(gas: number[], cost: number[]): number {
  const addAll = (acc: number, curr: number) => acc + curr;
  if (gas.reduce(addAll) < cost.reduce(addAll)) return -1;

  let currGain = 0;
  let answer = 0;

  gas.forEach((g, i) => {
    const c = cost.at(i) as number;
    currGain += g - c;

    if (currGain < 0) {
      currGain = 0;
      answer = i + 1;
    }
  });

  return answer;
}

export default () => {
  // const gas = [1, 2, 3, 4, 5];
  // const cost = [3, 4, 5, 1, 2];
  // const gas = [2, 3, 4];
  // const cost = [3, 4, 3];
  const gas = [4, 5, 2, 6, 5, 3];
  const cost = [3, 2, 7, 3, 2, 9];

  const result = canCompleteCircuit(gas, cost);
  console.log(result);
};
