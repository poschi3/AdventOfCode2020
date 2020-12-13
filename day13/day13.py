#!/usr/bin/env python3

import math

def wait_time(timestamp, id):
    return id - timestamp % id

with open('input.txt') as file:
    lines = file.read().splitlines()

timestamp = int(lines[0])
ids = lines[1].split(",")

results = []
for id in ids:
    if id != "x":
        results.append((int(id), wait_time(timestamp, int(id))))

minimum = min(results, key = lambda x: x[1] )
print(minimum[0] * minimum[1])
