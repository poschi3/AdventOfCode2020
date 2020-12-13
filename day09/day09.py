#!/usr/bin/env python3

from itertools import combinations, groupby
import math

# From: https://docs.python.org/3/library/itertools.html#itertools-recipes
def all_equal(iterable):
    g = groupby(iterable)
    print(g)
    return next(g, True) and not next(g, False)

def find_sum(previous, value):
    for combination in combinations(previous, 2):
        if sum(combination) == value:
            return True
    return False

def find_contiguous_sum(numbers, value):
    start_pointer = 0
    current_values = []
    while start_pointer <= len(numbers):
        current_pointer = start_pointer
        while sum(current_values) < value and current_pointer <= len(numbers):
            current_values.append(numbers[current_pointer])
            current_pointer += 1
        if sum(current_values) == value:
            return current_values
        current_values = []
        start_pointer += 1
    if current_pointer >= len(numbers):
        return None

def find(preamble_length, numbers):
    for i in range(preamble_length, len(numbers)):
        test_value = numbers[i]
        test_range = numbers[i-preamble_length:i]
        if not find_sum(test_range, test_value):
            return test_value

with open('input.txt') as file:
    numbers = [int(x) for x in file.read().splitlines()]

error_number = find(25, numbers)
print(error_number)
sum_area = find_contiguous_sum(numbers, error_number)
sum_area.sort()
print(sum_area[0] + sum_area[-1])
