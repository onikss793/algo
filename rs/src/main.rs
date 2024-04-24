use std::env;

mod summary_ranges;

fn main() {
    env::set_var("RUST_BACKTRACE", "1");
    summary_ranges::main();
}
