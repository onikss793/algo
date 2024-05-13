use std::env;

mod simplify_path;

fn main() {
    env::set_var("RUST_BACKTRACE", "1");
    simplify_path::main();
}
