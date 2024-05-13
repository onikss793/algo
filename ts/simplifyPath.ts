function simplifyPath(path: string): string {
  return (
    '/' +
    path
      .split('/')
      .reduce((result, p) => {
        if (!p.length || p === '.') {
          return result;
        }
        if (p === '..') {
          result.pop();
          return result;
        }

        result.push(p);
        return result;
      }, [] as string[])
      .join('/')
  );
}

export default () => {
  const path = '/a/./b/../../c/';
  // const path = '/.../a/../b/c/../d/./';
  // const path = '/../';
  // const path = '/home//foo/';
  // const path = '/home/';
  // const path = '/home/user/Documents/../Pictures';
  const result = simplifyPath(path);
  console.log(result);
};
