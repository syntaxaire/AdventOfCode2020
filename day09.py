# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/9

from collections import deque
from itertools import combinations


def solve_part1(lines):
    # preload window
    nums = deque()
    for line in range(25):
        nums.append(int(lines[line]))
    # begin validating numbers
    while True:
        line += 1
        if line > len(lines) - 1:
            break
        consider = int(lines[line])
        valid = False
        for pair in combinations(nums, 2):
            if (sum(pair) == consider) and (pair[0] != pair[1]):
                valid = True
                break
        if valid:
            nums.popleft()
            nums.append(consider)
        else:
            break
    return consider


def solve_part2(part1: int, lines: list[str]):
    for start_index, start_line in enumerate(lines):
        search_index = start_index + 1
        accum = int(start_line)
        while accum < part1:
            accum += int(lines[search_index])
            search_index += 1
        if accum == part1:
            int_lines = [int(line) for line in lines[start_index:search_index]]
            return min(int_lines) + max(int_lines)


if __name__ == '__main__':
    input_file = 'day09.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    part1_ans = solve_part1(input_lines)
    print('Part 1:', part1_ans)
    print('Part 2:', solve_part2(part1_ans, input_lines))
