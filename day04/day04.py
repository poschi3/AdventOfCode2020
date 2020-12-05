#!/usr/bin/env python3

import re

def check_passport_soft(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in required_fields:
        if field not in passport:
            return False
    return True

def check_in_range(value, least, most):
    number = int(value)
    return least <= number <= most

def check_height(value):
    unit = value[-2:]
    if unit == "cm":
        return check_in_range(value[:-2], 150, 193)
    if unit == "in":
        return check_in_range(value[:-2], 59, 76)
    return False

def check_passport_strong(passport):
    if not check_passport_soft(passport):
        return False

    if not check_in_range(passport["byr"], 1920, 2002):
        return False
    if not check_in_range(passport["iyr"], 2010, 2020):
        return False
    if not check_in_range(passport["eyr"], 2020, 2030):
        return False
    if not check_height(passport["hgt"]):
        return False
    
    if not re.match(r'^#[0-9a-f]{6}$', passport["hcl"]):
        return False

    hair_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not passport["ecl"] in hair_colors:
        return False

    if not re.match(r'^\d{9}$', passport["pid"]):
        return False
    return True

with open('input.txt') as file:
    raw_data = file.read()
    valid_soft = 0
    valid_strong = 0
    for raw_passport in  raw_data.split("\n\n"):
        passport = {}
        for datapoint in re.split(' |\n', raw_passport):
            datapoint = datapoint.strip()
            if datapoint:
                key_value = datapoint.split(":")
                passport[key_value[0]] = key_value[1]
        if check_passport_soft(passport):
            valid_soft += 1
        if check_passport_strong(passport):
            valid_strong += 1
    print(valid_soft)
    print(valid_strong)
