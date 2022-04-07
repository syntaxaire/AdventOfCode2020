"""Problem statement: https://adventofcode.com/2020/day/1"""
import itertools


def combinations_adding_to(nums, length, total):
    """Find all n-length combinations of nums that sum to total."""
    numset = set(nums)
    for combination in itertools.combinations(nums, length-1):
        numsum = sum(combination)
        target = total - numsum
        if target in numset:
            print(combination, target)
            return list(combination).append(target)

def solve_day1(inputs):
    ints = []
    for inputn in inputs:
        ints.append(int(inputn))
    for i in ints:
        for j in ints:
            for k in ints:
                if i + j + k == 2020:
                    return i, j, k


if __name__ == '__main__':
    with open('day01.input', 'r') as day1inputs:
        day1inputs = [int(x) for x in day1inputs.readlines()]
        print(combinations_adding_to(day1inputs, 3, 2020))
