use std::fs;

fn main() {
    println!("Starting puzzle 1!");
    let f = fs::read_to_string("input").unwrap();
    let input: Vec<&str> = f.split("\n").collect();
    // let input = [1721, 979, 366, 299, 675, 1456];
    part_one(&input);
    part_two(&input);
}

fn part_one(input: &Vec<&str>) {
    println!("Beginning Part One ...");
    for i in 0..(input.len() - 1) {
        for j in i..(input.len() - 1) {
            let curr_i: i32 = input[i].parse().unwrap();
            let curr_j: i32 = input[j].parse().unwrap();
            let curr_sum = curr_i + curr_j;

            if curr_sum == 2020 {
                println!("2020 sum found!");
                println!("Values are {} and {}", curr_i, curr_j);
                println!("Answer is {}", curr_i * curr_j);
            }
        }
    }
}

fn part_two(input: &Vec<&str>) {
    println!("Beginning Part Two ...");
    for i in 0..(input.len() - 1) {
        for j in i..(input.len() - 1) {
            for k in j..(input.len() - 1) {
                let curr_i: i32 = input[i].parse().unwrap();
                let curr_j: i32 = input[j].parse().unwrap();
                let curr_k: i32 = input[k].parse().unwrap();
                let curr_sum = curr_i + curr_j + curr_k;

                if curr_sum == 2020 {
                    println!("2020 sum found!");
                    println!("Values are {}, {}, {}", curr_i, curr_j, curr_k);
                    println!("Answer is {}", curr_i * curr_j * curr_k);
                }
            }
        }
    }
}
