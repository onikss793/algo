fn game_of_life(board: &mut Vec<Vec<i32>>) {
    let mut next_board = board.clone(); // Clone the board to store the next state

    for i in 0..board.len() {
        for j in 0..board[i].len() {
            let live_neighbors = count_live_neighbors(board, i, j);
            next_board[i][j] = next_state(board[i][j], live_neighbors);
        }
    }

    *board = next_board; // Replace the original board with the next state
}

fn count_live_neighbors(board: &Vec<Vec<i32>>, x: usize, y: usize) -> u8 {
    let mut count = 0;

    for i in (x as isize - 1)..=(x as isize + 1) {
        for j in (y as isize - 1)..=(y as isize + 1) {
            if i >= 0
                && j >= 0
                && i < board.len() as isize
                && j < board[x].len() as isize
                && (i != x as isize || j != y as isize)
            {
                if board[i as usize][j as usize] == 1 {
                    count += 1;
                }
            }
        }
    }

    count
}

fn next_state(cell: i32, live_neighbors: u8) -> i32 {
    match (cell, live_neighbors) {
        (1, 2) | (1, 3) => 1,
        (0, 3) => 1,
        _ => 0,
    }
}

pub fn main() {
    let mut board = vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];

    game_of_life(&mut board);
    println!("{:?}", board);
}

// struct CellState {
//     el: i32,
//     next_state: i32,
//     live_neighbors_count: i32,
// }
//
// fn cell_state(board: &Vec<Vec<i32>>, x: usize, y: usize) -> CellState {
//     let mut state = CellState {
//         el: board[x][y],
//         next_state: board[x][y],
//         live_neighbors_count: 0,
//     };
//
//     let mut plus_neighbor_count = |el: i32| {
//         if el == 1 {
//             state.live_neighbors_count += 1;
//         }
//     };
//
//     let row_len = board.len();
//     let col_len = board[0].len();
//
//     let get_neighbor = |x: isize, y: isize| -> i32 {
//         if x >= 0 && x < row_len as isize && y >= 0 && y < col_len as isize {
//             board[x as usize][y as usize]
//         } else {
//             0
//         }
//     };
//
//     plus_neighbor_count(get_neighbor(x as isize - 1, y as isize - 1));
//     plus_neighbor_count(get_neighbor(x as isize - 1, y as isize));
//     plus_neighbor_count(get_neighbor(x as isize - 1, y as isize + 1));
//
//     plus_neighbor_count(get_neighbor(x as isize, y as isize - 1));
//     plus_neighbor_count(get_neighbor(x as isize, y as isize + 1));
//
//     plus_neighbor_count(get_neighbor(x as isize + 1, y as isize - 1));
//     plus_neighbor_count(get_neighbor(x as isize + 1, y as isize));
//     plus_neighbor_count(get_neighbor(x as isize + 1, y as isize + 1));
//
//     if state.el == 1 {
//         if state.live_neighbors_count < 2 {
//             state.next_state = 0;
//         } else if state.live_neighbors_count > 3 {
//             state.next_state = 0;
//         }
//     } else {
//         if state.live_neighbors_count == 3 {
//             state.next_state = 1;
//         }
//     }
//
//     return state;
// }
//
// fn game_of_life(board: &mut Vec<Vec<i32>>) {
//     let state_map: Vec<Vec<CellState>> = board
//         .iter()
//         .enumerate()
//         .map(|(x, row)| {
//             return row
//                 .iter()
//                 .enumerate()
//                 .map(|(y, _)| cell_state(&board, x, y))
//                 .collect();
//         })
//         .collect();
//
//     for i in 0..board.len() {
//         for j in 0..board[i].len() {
//             board[i][j] = state_map[i][j].next_state
//         }
//     }
// }
//
// pub fn main() {
//     let mut board = vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];
//
//     game_of_life(&mut board);
//     println!("{:?}", board);
// }
