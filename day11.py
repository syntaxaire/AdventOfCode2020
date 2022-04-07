# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/11
from copy import deepcopy


def build_grid(lines: list[str]) -> list[list]:
    grid = []
    for line in lines:
        grid.append([char for char in line])
    return grid


def count_occupied_around(x, y, grid):
    """Occupied count with Part 1 parameters"""
    count = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if not (i == 0 and j == 0):
                try:
                    if (not y + j < 0) and (not x + i < 0):
                        if grid[y + j][x + i] == '#':
                            count += 1
                except IndexError:
                    pass
    return count


def count_occupied_around_part2(x, y, grid):
    """Occupied count, but with Part 2 parameters"""
    count = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if i == j and j == 0:
                continue  # zero vector
            # cast a ray in this direction
            a = x + i  # ray current x
            b = y + j  # ray current y
            occupied = False
            # bounds checking
            while not(b < 0 or a < 0 or b >= len(grid) or a >= len(grid[0])):
                if grid[b][a] == '#':
                    occupied = True
                    break
                elif grid[b][a] == 'L':
                    break
                a += i
                b += j
            if occupied:
                count += 1
    return count


def sim(grid):
    """Simulate grid with Part 1 rules"""
    new_grid = deepcopy(grid)
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 'L':
                if count_occupied_around(x, y, grid) == 0:
                    new_grid[y][x] = '#'
            elif square == '#':
                if count_occupied_around(x, y, grid) >= 4:
                    new_grid[y][x] = 'L'
    return new_grid


def sim_part2(grid):
    """Simulate grid with Part 2 rules"""
    new_grid = deepcopy(grid)
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 'L':
                if count_occupied_around_part2(x, y, grid) == 0:
                    new_grid[y][x] = '#'
            elif square == '#':
                if count_occupied_around_part2(x, y, grid) >= 5:
                    new_grid[y][x] = 'L'
    return new_grid


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()


def grid_same(grid1, grid2):
    for j in range(len(grid1)):
        for i in range(len(grid1[0])):
            if grid1[j][i] != grid2[j][i]:
                return False
    return True


def count_occupied(grid):
    count = 0
    for j, row in enumerate(grid):
        for i, square in enumerate(row):
            if square == '#':
                count += 1
    return count


def solve_part1(lines):
    grid = build_grid(lines)
    while True:
        new_grid = sim(grid)
        if grid_same(grid, new_grid):
            return count_occupied(grid)
        grid = new_grid


def solve_part2(lines):
    grid = build_grid(lines)
    while True:
        new_grid = sim_part2(grid)
        if grid_same(grid, new_grid):
            return count_occupied(grid)
        grid = new_grid


if __name__ == '__main__':
    input_file = 'day11.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
