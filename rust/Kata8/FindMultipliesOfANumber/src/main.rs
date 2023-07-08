fn find_multiplies(n: u32, limit: u32) -> Vec<u32> {
    let mut res = vec![];
    (n..=limit).step_by(n as usize).for_each(|i| res.push(i));
    res
}

fn main() {
    println!("{:?}", find_multiplies(5, 7))
}
