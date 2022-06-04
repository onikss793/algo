class RandomizedSet {
  private data: Map<number, number>;
  private indexes: number[];

  constructor() {
    this.data = new Map();
    this.indexes = [];
  }

  insert(val: number): boolean {
    if (this.data.has(val)) return false;

    const index = this.indexes.length;
    this.data.set(val, index);
    this.indexes.push(val);

    return true;
  }

  remove(val: number): boolean {
    const index = this.data.get(val);
    if (index === undefined) return false;
    const lastIndex = this.indexes.length - 1;

    if (index !== lastIndex) {
      const last = this.indexes[lastIndex];
      this.indexes[index] = last;

      this.data.set(last, index);
    }

    this.indexes.pop();
    this.data.delete(val);

    return true;
  }

  getRandom(): number {
    return this.indexes[Math.floor(Math.random() * this.data.size)];
  }

  log() {
    console.log({
      indexes: this.indexes,
      data: this.data,
    });
    return 'log';
  }
}

export default () => {
  const obj = new RandomizedSet();

  console.log([
    obj.insert(0),
    obj.insert(10),
    obj.insert(20),
    obj.insert(30),
    obj.log(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
    obj.getRandom(),
  ]);
};
