#!/usr/bin/env python3

def prccede_group(raw_group):
    group = {}
    for raw_passenger in raw_group.split("\n"):
        for answer in raw_passenger.strip():
            group[answer] = True
    return len(group)

sum = 0
with open('input.txt') as file:
    raw_data = file.read()
    for raw_group in raw_data.split("\n\n"):
        sum += prccede_group(raw_group)
       
print(sum)
