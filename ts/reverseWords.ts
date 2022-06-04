function reverseWords(s: string): string {
  return s
    .split(' ')
    .filter(it => !!it.length)
    .reverse()
    .join(' ');
}

export default () => {
  const s = 'a good   example';
  const result = reverseWords(s);
  console.log(result);
};
