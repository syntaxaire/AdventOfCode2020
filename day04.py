# Advent of Code solution
# Problem statement: https://adventofcode.com/2020/day/4

import re

def parse_record(lines):
    fields = ' '.join(lines).split(' ')
    record = {}
    for field in fields:
        name, value = field.split(':')
        record[name] = value
    return record


def parse_file(lines):
    record_lines = []
    records = []
    for record_line in lines:
        if record_line != '':
            record_lines.append(record_line)
        else:
            records.append(parse_record(record_lines))
            record_lines = []
    records.append(parse_record(record_lines))  # record last record
    return records


def has_valid_fields(record: dict):
    for key, value in record.items():
        if key == 'byr':
            if not value.isdigit():
                return False
            if not len(value) == 4:
                return False
            if not 1920 <= int(value) <= 2002:
                return False
        if key == 'iyr':
            if not value.isdigit():
                return False
            if not len(value) == 4:
                return False
            if not 2010 <= int(value) <= 2020:
                return False
        if key == 'eyr':
            if not value.isdigit():
                return False
            if not len(value) == 4:
                return False
            if not 2020 <= int(value) <= 2030:
                return False
        if key == 'hgt':
            match = re.fullmatch(r'(\d+)(cm|in)', value)
            if match is None:
                return False
            height, unit = match.group(1, 2)
            height = int(height)
            if unit == 'cm':
                if not 150 <= height <= 193:
                    return False
            elif unit == 'in':
                if not 59 <= height <= 76:
                    return False
            else:
                return False
        if key == 'hcl':
            match = re.fullmatch(r'#(\d|[a-f]){6}', value)
            if match is None:
                return False
        if key == 'ecl':
            if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
        if key == 'pid':
            match = re.fullmatch(r'\d{9}', value)
            if match is None:
                return False
        if key == 'cid':
            pass
    return True


def solve_part1(lines):
    records = parse_file(lines)
    req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0
    for record in records:
        if all(req_field in record for req_field in req_fields):
            valid += 1
    return valid


def solve_part2(lines):
    records = parse_file(lines)
    req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0
    for record in records:
        if all(req_field in record for req_field in req_fields):
            if has_valid_fields(record):
                valid += 1
    return valid


if __name__ == '__main__':
    input_file = 'day04.input'
    input_lines = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            input_lines.append(line.strip())
    print('Part 1:', solve_part1(input_lines))
    print('Part 2:', solve_part2(input_lines))