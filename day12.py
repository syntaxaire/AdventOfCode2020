# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/12
from collections import deque


def solve_part1(lines):
    x = 0
    y = 0
    e, s, w, n = (1, 0), (0, -1), (-1, 0), (0, 1)
    vectors = {'E': e, 'S': s, 'W': w, 'N': n}
    facing = deque((e, s, w, n))
    for line in lines:
        action, quantity = line[0], int(line[1:])
        if action == 'L' or action == 'R':
            nineties = int(quantity / 90)
            facing.rotate(nineties if action == 'L' else -nineties)
        elif action == 'F':
            x += facing[0][0] * quantity
            y += facing[0][1] * quantity
        else:
            x += vectors[action][0] * quantity
            y += vectors[action][1] * quantity
    return abs(x) + abs(y)


def solve_part2(lines):
    way_x = 10
    way_y = 1
    ship_x = 0
    ship_y = 0
    e, s, w, n = (1, 0), (0, -1), (-1, 0), (0, 1)
    vectors = {'E': e, 'S': s, 'W': w, 'N': n}
    for line in lines:
        action, quantity = line[0], int(line[1:])
        if action == 'L' or action == 'R':
            if line == 'R90' or line == 'L270':
                way_x, way_y = way_y, -way_x
            elif line == 'R180' or line == 'L180':
                way_x, way_y = -way_x, -way_y
            elif line == 'R270' or line == 'L90':
                way_x, way_y = -way_y, way_x
            else:
                raise ValueError
        elif action == 'F':
            ship_x += quantity * way_x
            ship_y += quantity * way_y
        else:
            way_x += vectors[action][0] * quantity
            way_y += vectors[action][1] * quantity
    return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    input_file = 'day12.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
