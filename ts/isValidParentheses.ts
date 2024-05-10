class Stack {
  private state: string[] = [];

  push(char: string) {
    if (char === ')') return this.handleA(char);
    if (char === '}') return this.handleB(char);
    if (char === ']') return this.handleC(char);

    this.handleOpeners(char);
  }

  private handleOpeners(char: string) {
    this.state.push(char);
    this.logState();
  }

  private handleA(char: string) {
    if (this.last === '(') {
      this.state.pop();
    } else {
      this.state.push(char);
    }

    this.logState();
  }

  private handleB(char: string) {
    if (this.last === '{') {
      this.state.pop();
    } else {
      this.state.push(char);
    }
    this.logState();
  }

  private handleC(char: string) {
    if (this.last === '[') {
      this.state.pop();
    } else {
      this.state.push(char);
    }
    this.logState();
  }

  private logState() {
    console.log(this.state);
  }

  public get length() {
    return this.state.length;
  }

  private get last() {
    return this.state.at(this.state.length - 1);
  }
}

const brackets = {
  ')': '(',
  '}': '{',
  ']': '[',
} as const;
const openers = ['(', '{', '['] as const;
const stack: string[] = [];

function isValidParentheses(s: string): boolean {
  for (let i = 0; i < s.length; i++) {
    const bracket = s[i] as keyof typeof brackets &
      (typeof brackets)[keyof typeof brackets];

    if (openers.includes(bracket)) {
      stack.push(bracket);
    } else if (stack.pop() !== brackets[bracket]) {
      return false;
    }
  }

  return stack.length === 0;
}

export default () => {
  const s = '{[]}';
  // const s = '(])';
  // const s = '(]';
  // const s = '()[]{}';
  // const s = '()';
  const result = isValidParentheses(s);
  console.log(result);
};
