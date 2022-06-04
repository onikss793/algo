/**
 Do not return anything, modify board in-place instead.
 */
function gameOfLife(board: number[][]): void {
  const stateMap = board.map((row, x) => {
    return row.map((el, y) => {
      return cellState(el, x, y);
    });
  });

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      board[i][j] = stateMap[i][j].nextState;
    }
  }

  function cellState(live: number, x: number, y: number) {
    const state: { el: number; nextState: number; liveNeighborsCount: number } =
      {
        el: board[x][y],
        nextState: board[x][y],
        liveNeighborsCount: 0,
      };

    if (board[x - 1] !== undefined) {
      plusNeighborCount(board[x - 1][y - 1]);
      plusNeighborCount(board[x - 1][y]);
      plusNeighborCount(board[x - 1][y + 1]);
    }

    if (board[x] !== undefined) {
      plusNeighborCount(board[x][y - 1]);
      plusNeighborCount(board[x][y + 1]);
    }

    if (board[x + 1] !== undefined) {
      plusNeighborCount(board[x + 1][y - 1]);
      plusNeighborCount(board[x + 1][y]);
      plusNeighborCount(board[x + 1][y + 1]);
    }

    live ? stateForLive() : stateForDead();

    return state;

    function plusNeighborCount(el?: number) {
      if (el === 1) state.liveNeighborsCount += 1;
    }
    function stateForLive() {
      if (state.liveNeighborsCount < 2) state.nextState = 0;
      if (state.liveNeighborsCount === 2 || state.liveNeighborsCount === 3)
        state.nextState = 1;
      if (state.liveNeighborsCount > 3) state.nextState = 0;
    }
    function stateForDead() {
      if (state.liveNeighborsCount === 3) state.nextState = 1;
    }
  }
}

export default () => {
  const board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
  ];
  gameOfLife(board);
  console.log(board);
};
