# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/6


def get_groups(lines):
    groups = []
    group_answer = []
    for line in lines:
        if len(line) > 0:
            group_answer.append(line)
        else:
            groups.append(group_answer)
            group_answer = []
    groups.append(group_answer)  # read last group
    return groups


def solve_part1(lines):
    groups = get_groups(lines)
    answer_sum = 0
    for group in groups:
        answers = set()
        for answer in group:
            answers = answers | set(answer)
        answer_sum += len(answers)
    return answer_sum


def solve_part2(lines):
    groups = get_groups(lines)
    answer_sum = 0
    all_group_answers = []
    for group in groups:
        group_answers = []
        for person in group:
            group_answers.append(set(person))
        all_group_answers.append(group_answers)
    for group in all_group_answers:
        intersection = set.intersection(*group)
        answer_sum += len(intersection)
    return answer_sum


if __name__ == '__main__':
    input_file = 'day06.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for readline in f.readlines():
            input_lines.append(readline.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))
