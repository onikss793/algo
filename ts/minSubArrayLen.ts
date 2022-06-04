function minSubArrayLen(target: number, nums: number[]): number {
  let minLength = Infinity;
  let sum = 0;
  let left = 0;

  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];

    // 현재 합이 타겟 이상이면서 최소 길이인지 확인
    while (sum >= target) {
      minLength = Math.min(minLength, right - left + 1);
      sum -= nums[left]; // 윈도우의 왼쪽 끝을 이동하여 길이를 줄임
      left++;
    }
  }

  // minLength가 초기값인 Infinity일 경우, 합이 타겟 이상인 부분 배열이 없는 것이므로 0을 반환
  return minLength === Infinity ? 0 : minLength;
}

export default () => {
  // const target = 7;
  // const nums = [1, 1, 1, 1, 7];
  // const target = 213;
  // const nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12];
  // const target = 20;
  // const nums = [2, 16, 14, 15];
  // const target = 15;
  // const nums = [1, 2, 3, 4, 5];
  const target = 7;
  const nums = [2, 3, 1, 2, 4, 3];
  const result = minSubArrayLen(target, nums);
  console.log(result);
};
