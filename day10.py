# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/10

def load_adapters(lines):
    adapters = [int(line) for line in lines]
    adapters.sort()
    return adapters


def solve_part1(lines):
    adapters = load_adapters(lines)
    adapters.append(adapters[-1] + 3)  # append final adapter to list
    diff1 = 0
    diff3 = 0
    previous = 0
    for adapter in adapters:
        if adapter - previous == 1:
            diff1 += 1
        if adapter - previous == 3:
            diff3 += 1
        previous = adapter
    return diff1 * diff3


def solve_part2(lines):
    loaded_adapters = load_adapters(lines)
    adapters = [0]
    adapters.extend(loaded_adapters)  # add initial adapter to list
    # strategy: iterate backwards from final adapter and use lookups
    index = {}
    total = 0
    top_target = adapters[-1] + 3
    for adapter in adapters[::-1]:
        current = 0
        for i in range(1, 4):
            # if we can reach the max number directly, add 1
            # otherwise for each intermediary found, add the number of paths through that
            if adapter + i == top_target:
                current += 1
            elif adapter + i in index:
                current += index[adapter + i]
        index[adapter] = current
    return index[0]


if __name__ == '__main__':
    input_file = 'day10.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
