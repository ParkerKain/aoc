use std::fs;

use regex::Regex;

fn main() {
    println!("Beginning Day 2");
    let f = fs::read_to_string("input").unwrap();
    let input: Vec<&str> = f.split('\n').collect();
    // let input: Vec<&str> = vec!["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"];
    // part_one(input);
    part_two(input);
}

#[derive(Debug)]
struct Input<'a> {
    min: usize,
    max: usize,
    letter: char,
    string: &'a str,
}

impl<'a> Input<'a> {
    fn solve_pt1(&self) -> u16 {
        let mut curr_occurances = 0;
        for c in self.string.chars() {
            if c == self.letter {
                curr_occurances += 1;
                if curr_occurances > self.max {
                    return 0;
                }
            }
        }
        match curr_occurances >= self.min {
            false => 0,
            true => 1,
        }
    }

    fn solve_pt2(&self) -> u16 {
        let match_min: u16 = (self.string.chars().nth(self.min - 1).unwrap() == self.letter) as u16;
        let match_max: u16 = (self.string.chars().nth(self.max - 1).unwrap() == self.letter) as u16;

        (match_min + match_max) % 2
    }
}

fn _parse_input_line(line: &str) -> Input {
    let re = Regex::new(r"-| |:").unwrap();
    let fields: Vec<&str> = re.split(line).collect();

    let min: usize = fields[0].parse().unwrap();
    let max: usize = fields[1].parse().unwrap();
    let letter: char = fields[2].chars().next().unwrap();
    let string = fields[4];
    Input {
        min,
        max,
        letter,
        string,
    }
}

fn part_one(input: Vec<&str>) {
    let mut answer: u16 = 0;
    for row in input {
        if row.is_empty() {
            break;
        }
        let cleaned_input: Input = _parse_input_line(row);
        answer += cleaned_input.solve_pt1();
    }
    println!("Final Part One Answer: {}", answer);
}

fn part_two(input: Vec<&str>) {
    let mut answer: u16 = 0;
    for row in input {
        if row.is_empty() {
            break;
        }
        let cleaned_input: Input = _parse_input_line(row);
        answer += cleaned_input.solve_pt2();
    }
    println!("Final Part Two Answer: {}", answer);
}
