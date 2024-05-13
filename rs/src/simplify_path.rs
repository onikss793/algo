fn simplify_path(path: String) -> String {
    let result: Vec<&str> = vec![];
    return "/".to_owned()
        + &path
            .split('/')
            .fold(result, |mut result, p| match p {
                "" => {
                    return result;
                }
                "." => {
                    return result;
                }
                ".." => {
                    result.pop();
                    return result;
                }
                p => {
                    result.push(p);
                    return result;
                }
            })
            .join("/");
}

pub fn main() {
    let path: String = "/a/./b/../../c/".to_string();
    // let path: String = "/.../a/../b/c/../d/./".to_string();
    let result = simplify_path(path);
    println!("{result}");
}
