#!/usr/bin/env python3

pos_x = 0
go_right = 3
trees = 0

with open('input.txt') as file:
    for mapline in file.readlines():
        if mapline[pos_x%(len(mapline)-1)] == "#":
            trees += 1
        pos_x += go_right
print(trees)
