#!/usr/bin/env python3

import re

# 5-8 j: jjjjjjjjjgjjjjjjjjj
exp = re.compile(r'(\d+)-(\d+) (.): (.+)')

def check_a(policy):
    m = exp.match(policy)
    min = int(m.group(1))
    max = int(m.group(2))
    pattern = m.group(3)
    password = m.group(4)
    
    count = 0
    for letter in password:
        if(pattern == letter):
            count += 1
    return count >= min and count <= max

def check_b(policy):
    m = exp.match(policy)
    position_a = int(m.group(1))
    position_b = int(m.group(2))
    pattern = m.group(3)
    password = m.group(4)
    
    return (password[position_a-1] == pattern) ^ (password[position_b-1] == pattern)

count_a = 0
count_b = 0
with open('input.txt') as file:
    for policy in file.readlines():
        if(check_a(policy)):
            count_a += 1
        if(check_b(policy)):
            count_b += 1

print(str(count_a))
print(str(count_b))
