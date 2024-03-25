use std::{fs, vec};

use regex::Regex;

fn main() {
    println!("Beginning Day 2");
    let f = fs::read_to_string("input").unwrap();
    // let input: Vec<&str> = f.split("\n").collect();
    let input: Vec<&str> = vec!["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"];
    part_one(input);
    part_two();
}

#[derive(Debug)]
struct Input<'a> {
    min: u16,
    max: u16,
    letter: char,
    string: &'a str,
}

fn _parse_input_line(line: &str) -> Input {
    let re = Regex::new(r"-| |:").unwrap();
    let fields: Vec<&str> = re.split(line).collect();

    let min: u16 = fields[0].parse().unwrap();
    let max: u16 = fields[1].parse().unwrap();
    let letter: char = fields[2].chars().next().unwrap();
    let string = fields[4];
    let cleaned_input: Input = Input {
        min,
        max,
        letter,
        string,
    };

    return cleaned_input;
}

fn part_one(input: Vec<&str>) {
    for row in input {
        let cleaned_input: Input = _parse_input_line(row);
        println!("{:?}", cleaned_input);
    }
}

fn part_two() {}
