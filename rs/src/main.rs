use std::env;

mod find_min_arrow_shots;

fn main() {
    env::set_var("RUST_BACKTRACE", "1");
    find_min_arrow_shots::main();
}
