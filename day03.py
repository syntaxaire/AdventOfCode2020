# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/3

def count_trees(inc_x, inc_y, lines):
    cur_x, cur_y = 0, 0
    cur_x += inc_x
    cur_y += inc_y
    hits = 0
    while cur_y < len(lines):
        if cur_x > len(lines[0]) - 1:
            cur_x -= len(lines[0])
        if lines[cur_y][cur_x] == '#':
            hits += 1
        cur_x += inc_x
        cur_y += inc_y
    return hits


def solve_part1(lines):
    return count_trees(3, 1, lines)


def solve_part2(lines):
    slope_1 = count_trees(1, 1, lines)
    slope_2 = count_trees(3, 1, lines)
    slope_3 = count_trees(5, 1, lines)
    slope_4 = count_trees(7, 1, lines)
    slope_5 = count_trees(1, 2, lines)
    return slope_1 * slope_2 * slope_3 * slope_4 * slope_5


if __name__ == '__main__':
    input_file = 'day03.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            input_lines.append(line.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
