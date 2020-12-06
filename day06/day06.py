#!/usr/bin/env python3

def procede_group_or(raw_group):
    group = {}
    for raw_passenger in raw_group.split("\n"):
        for answer in raw_passenger.strip():
            group[answer] = True
    return len(group)

def procede_group_and(raw_group):
    group = {}
    for raw_passenger in raw_group.split("\n"):
        for answer in raw_passenger.strip():
            group[answer] = group[answer] + 1 if answer in group else 1
    
    passengers = raw_group.count("\n") + 1
    yeses = 0
    for answers in group.values():
        if answers >= passengers:
            yeses += 1
    return yeses

sum_or = 0
sum_and = 0
with open('input.txt') as file:
    raw_data = file.read()
    for raw_group in raw_data.split("\n\n"):
        sum_or += procede_group_or(raw_group.strip())
        sum_and += procede_group_and(raw_group.strip())
       
print(sum_or)
print(sum_and)
