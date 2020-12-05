#!/usr/bin/env python3

def count_trees(map, slope):
    go_right = slope[0]
    go_down = slope[1]
    pos_x = 0
    pos_y = 0
    trees = 0
    while pos_y < len(map):
        mapline = map[pos_y]
        if mapline[pos_x%(len(mapline))] == "#":
            trees += 1
        pos_x += go_right
        pos_y += go_down
    return trees

slopes = [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]

multiplied_trees = 1
with open('input.txt') as file:
    map = file.read().splitlines()
    for slope in slopes:
        trees = count_trees(map, slope)
        print(str(slope) + ": " + str(trees))
        multiplied_trees *= trees
        
print(multiplied_trees)
