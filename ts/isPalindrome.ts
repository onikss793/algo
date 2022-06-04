function isPalindrome(s: string): boolean {
  const replaced = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  return replaced === replaced.split('').reverse().join('');

  //   const replaced = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  //
  //   let j = replaced.length - 1;
  //   for (let i = 0; i < j; i++) {
  //     if (replaced[i] !== replaced[j]) {
  //       return false;
  //     }
  //
  //     j -= 1;
  //   }
  //
  //   return true;

  //   const regex = new RegExp(/[a-z0-9]/);
  //   const filtered = Array.from(s, str => str.toLowerCase()).filter(str => {
  //     return regex.test(str);
  //   });
  //
  //   let j = filtered.length - 1;
  //
  //   for (let i = 0; i < j; i++) {
  //     if (filtered[i] !== filtered[j]) {
  //       return false;
  //     }
  //
  //     j -= 1;
  //   }
  //
  //   return true;
}

export default () => {
  const s = 'A man, a plan, a canal: Panama';
  // const s = 'race a car';
  // const s = ' ';
  // const s = 'aA ';
  const result = isPalindrome(s);
  console.log(result);
};
