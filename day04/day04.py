#!/usr/bin/env python3

import re

def check_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"
    for field in required_fields:
        if field not in passport:
            return False
    return True

with open('input.txt') as file:
    raw_data = file.read()
    valid = 0
    for raw_passport in  raw_data.split("\n\n"):
        passport = {}
        for datapoint in re.split(' |\n', raw_passport):
            datapoint = datapoint.strip()
            if datapoint:
                key_value = datapoint.split(":")
                passport[key_value[0]] = key_value[1]
        if check_passport(passport):
            valid += 1
    print(valid)
