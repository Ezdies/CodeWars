fn remove_smallest(numbers: &[u32]) -> Vec<u32>{
    let mini = numbers.iter().min().unwrap_or(&0);
    numbers.iter().take_while(|x| x > &mini).collect()
    
}


fn main() {
    let arr = [2, 2, 1, 2, 1];
    println!("{:?}", remove_smallest(&arr));
}
