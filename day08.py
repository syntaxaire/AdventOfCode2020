# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/8

def find_acc_on_loop(lines):
    line = 0
    acc = 0
    visited = set()
    while True:
        if line in visited:
            break
        else:
            visited.add(line)
        op, val = lines[line].split()
        if op == 'acc':
            acc += int(val)
        if op == 'jmp':
            line += int(val)
        else:
            line += 1
    return acc


def solve_part1(lines):
    return find_acc_on_loop(lines)


def sim_part2(lines):
    line = 0
    acc = 0
    visited = set()
    while True:
        if line in visited:
            return False, acc
        else:
            visited.add(line)
        if line == len(lines):
            return True, acc
        if line > len(lines):
            return False, acc
        op, val = lines[line].split()
        if op == 'acc':
            acc += int(val)
        if op == 'jmp':
            line += int(val)
        else:
            line += 1


def solve_part2(lines):
    for index, line in enumerate(lines):
        lines_copy = list(lines)
        op, val = line.split()
        if op == 'jmp':
            lines_copy[index] = 'nop ' + val
        elif op == 'nop':
            lines_copy[index] = 'jmp ' + val
        result, acc = sim_part2(lines_copy)
        if result:
            return acc


if __name__ == '__main__':
    input_file = 'day08.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
