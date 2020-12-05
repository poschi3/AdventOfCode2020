#!/usr/bin/env python3

def decode_row(row):
    return int(row.replace("F", "0").replace("B", "1"), 2)

def decode_column(column):
    return int(column.replace("L", "0").replace("R", "1"), 2)

max = 0
taken = {}
with open('input.txt') as file:
    for boarding_pass in file.readlines():
        row = decode_row(boarding_pass[0:7])
        column = decode_column(boarding_pass[7:10])
        seat = row * 8 + column
        taken[seat] = True
        if max < seat:
            max = seat
print(max)

for seat in range(1, max-1):
    if seat not in taken and seat-1 in taken and seat+1 in taken:
        print(seat)
