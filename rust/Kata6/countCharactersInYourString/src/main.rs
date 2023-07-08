use std::collections::HashMap;

fn count(input: &str) -> HashMap<char, i32>{
    let mut my_map = HashMap::new();
    for c in input.chars(){
        *my_map.entry(c).or_insert(0) += 1;
    }
    my_map
}

fn main() {
    println!("Hello, world!");
}
