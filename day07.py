# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/7

from collections import defaultdict


def build_bag_registry(lines):
    bag_registry = {}
    colors = set()
    for line in lines:
        color, contents = line.split(' bags contain ')
        sub_bags = {}
        temp_bags = []
        contents = contents.split(', ')
        for content in contents:
            bag_loc = content.find(' bag')
            snip = content[:bag_loc]
            temp_bags.append(snip)
        for sub_bag in temp_bags:
            if sub_bag == 'no other':
                sub_bags.update({'no other': 0})
            else:
                sub_number, sub_color = sub_bag.split(maxsplit=1)
                sub_bags.update({sub_color: int(sub_number)})
        bag_registry[color] = sub_bags
    return bag_registry


def build_bag_reverse_tree(bag_registry):
    bag_reverse = defaultdict(list)
    for outer_color, inners in bag_registry.items():
        for inner_color, inner_quant in inners.items():
            if inner_color == 'no other':
                continue
            bag_reverse[inner_color].append(outer_color)
    return bag_reverse


def find_parents(color: str, bag_tree: dict) -> list:
    """Find total valid containers for a color using the reverse tree."""
    if len(bag_tree[color]) > 0:
        parents = list(bag_tree[color])
    else:
        return []
    for parent in parents:
        further_parents = find_parents(parent, bag_tree)
        if len(further_parents) > 0:
            parents.extend(further_parents)
    return parents


def find_children(color: str, bag_registry: dict) -> int:
    """Find total number of children of a bag."""
    count = 0
    for key, value in bag_registry[color].items():
        if key == 'no other':
            continue
        count += value
        count += find_children(key, bag_registry) * value
    return count


def solve_part1(lines):
    bag_registry = build_bag_registry(lines)
    bag_tree = build_bag_reverse_tree(bag_registry)
    valid_parents = find_parents('shiny gold', bag_tree)
    return len(set(valid_parents))


def solve_part2(lines):
    bag_registry = build_bag_registry(lines)
    children = find_children('shiny gold', bag_registry)
    return children


if __name__ == '__main__':
    input_file = 'day07.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
