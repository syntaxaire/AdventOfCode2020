# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/1

def solve_part1(lines):
    pass


def solve_part2(lines):
    pass


if __name__ == '__main__':
    input_file = 'day01.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
