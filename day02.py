"""Problem statement: https://adventofcode.com/2020/day/2"""

def solve_day2(lines):
    valid = 0
    for line in lines:
        line = line.strip()
        counts, letter, password = line.split()
        letter = letter[0]
        lower_s, upper_s = counts.split('-')
        lower = int(lower_s)
        upper = int(upper_s)
        count = password.count(letter)
        if lower <= count <= upper:
            print(f'  valid: {line}')
            valid += 1
        else:
            print(f'invalid: {line}')
    return valid

def solve_day2_part2(lines):
    valid = 0
    for line in lines:
        line = line.strip()
        positions, letter, password = line.split()
        letter = letter[0]
        position1_s, position2_s = positions.split('-')
        position1 = int(position1_s)
        position2 = int(position2_s)
        if (password[position1-1] == letter and password[position2-1] != letter) or \
            (password[position1-1] != letter and password[position2-1] == letter):
            print(f'  valid: {line}')
            valid += 1
        else:
            print(f'invalid: {line}')
    return valid

if __name__ == '__main__':
    with open('day02.input', 'r') as day2inputs:
        lines = day2inputs.readlines()
        print(solve_day2(lines))
        print(solve_day2_part2(lines))
