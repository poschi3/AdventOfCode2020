#!/usr/bin/env python3

import re

exp = re.compile(r'(\d+)-(\d+) (.): (.+)')

# 5-8 j: jjjjjjjjjgjjjjjjjjj
def check(policy):
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

count = 0
with open('input.txt') as file:
    for policy in file.readlines():
        if(check(policy)):
            count += 1

print(str(count))
