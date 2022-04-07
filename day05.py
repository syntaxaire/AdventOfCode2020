# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/5

def decode_pass(code):
    row_code, seat_code = code[:7], code[7:]
    row_code = row_code.replace('F', '0')
    row_code = row_code.replace('B', '1')
    row = int(row_code, 2)
    seat_code = seat_code.replace('L', '0')
    seat_code = seat_code.replace('R', '1')
    seat = int(seat_code, 2)
    return row, seat


def solve_part1(lines):
    seat_numbers = []
    for line in lines:
        row, seat = decode_pass(line)
        seat_numbers.append(row * 8 + seat)
    return max(seat_numbers)


def solve_part2(lines):
    seat_numbers = []
    for line in lines:
        row, seat = decode_pass(line)
        seat_numbers.append(row * 8 + seat)
    lowest_seat = min(seat_numbers)
    highest_seat = max(seat_numbers)
    seat_range = range(lowest_seat, highest_seat + 1)
    possible_seats = set(seat_range)
    actual_seats = set(seat_numbers)
    return possible_seats - actual_seats


if __name__ == '__main__':
    input_file = 'day05.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
