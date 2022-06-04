function maxProfit(prices: number[]): number {
  let i = 0;
  let j = i + 1;
  const arr = [0];

  while (i < prices.length - 1) {
    const buy = prices[i];
    const sell = prices[j];
    const profit = sell - buy;

    console.log({ [i]: buy, [j]: sell, arr });

    if (profit < 0) {
      i = j;
      j = i + 1;
      continue;
    }

    i = j;
    j = i + 1;

    arr.push(profit);
  }

  return arr.reduce((acc, curr) => acc + curr);
}

export default () => {
  // const prices = [7, 1, 5, 3, 6, 4];
  // const prices = [1, 2, 3, 4, 5];
  const prices = [7, 6, 4, 3, 1];

  const result = maxProfit(prices);
  console.log(result);
};
