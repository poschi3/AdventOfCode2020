#!/usr/bin/env python3

import copy

def get_pos(seats, x, y):
    if x >= len(seats) or x < 0:
        return "|"
    row = seats[x]
    if y >= len(row) or y < 0:
        return "|"
    return row[y]

arounds = [
    (0, -1), (0, +1), # left / right
    (+1, 0), (-1, 0), # top / bottom
    (+1, +1), (+1, -1),
    (-1, -1), (-1, +1)
]
def number_occupied_arround(seats, x, y):
    neighbours = []
    for around in arounds:
        neighbours.append(get_pos(seats, x + around[0], y + around[1]))
    return neighbours.count("#")

def number_occupied_see(seats, x, y):
    neighbours = []
    for around in arounds:
        new_x = x
        new_y = y
        see = "."
        while see == ".":
            new_x += around[0]
            new_y += around[1]
            see = get_pos(seats, new_x, new_y)
        neighbours.append(see)
    return neighbours.count("#")

def calc_round(seats, number_method, occupied_max):
    new_seats = []
    for x, row in enumerate(seats):
        new_row = ""
        for y, actual in enumerate(row):
            occupied = number_method(seats, x, y)
            if actual == "L":
                if occupied == 0:
                    new_row += "#"
                else:
                    new_row += "L"
            elif actual == "#":
                if occupied >= occupied_max:
                    new_row += "L"
                else:
                    new_row += "#"
            else:
                new_row += "."
        new_seats.append(new_row)
    return new_seats

with open('input.txt') as file:
    seats = file.read().splitlines()

new_seats = []

def print_seats(seats):
    for seat in seats:
        print(seat)

seats_a = copy.deepcopy(seats)
while True:
    new_seats = calc_round(seats_a, number_occupied_arround, 4)
    if seats_a == new_seats:
        break
    seats_a = new_seats

occupied = sum([row.count("#") for row in seats_a])
print(occupied)

seats_b = copy.deepcopy(seats)
while True:
    new_seats = calc_round(seats_b, number_occupied_see, 5)
    if seats_b == new_seats:
        break
    seats_b = new_seats

occupied_b = sum([row.count("#") for row in seats_b])
print(occupied_b)
