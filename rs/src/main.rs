use std::env;

mod is_valid_parentheses;

fn main() {
    env::set_var("RUST_BACKTRACE", "1");
    is_valid_parentheses::main();
}
