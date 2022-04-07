# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/13

def solve_part1(lines):
    cur_time = int(lines[0])
    buses = lines[1].split(',')
    buses = [int(bus) for bus in buses if bus != 'x']
    min_bus_id = 0
    min_bus_time = 99999999999999
    for bus_id in buses:
        bus_next_time = (cur_time // bus_id) * bus_id
        if bus_next_time < cur_time:
            bus_next_time += bus_id
        if bus_next_time < min_bus_time:
            min_bus_time = bus_next_time
            min_bus_id = bus_id
    return min_bus_id * (min_bus_time - cur_time)


def solve_part2(lines):
    buses = '7,13,x,x,59,x,31,19'.split(',')
    bus_pos = []
    for position, bus in enumerate(buses):
        if bus != 'x':
            bus_pos.append((int(bus), position))
    



if __name__ == '__main__':
    input_file = 'day13.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
#     input_lines = """939
# 7,13,x,x,59,x,31,19""".split('\n')
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
