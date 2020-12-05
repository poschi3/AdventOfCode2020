#!/usr/bin/env python3

def decode_row(row):
    return int(row.replace("F", "0").replace("B", "1"), 2)

def decode_column(column):
    return int(column.replace("L", "0").replace("R", "1"), 2)

max = 0
with open('input.txt') as file:
    for boarding_pass in file.readlines():
        boarding_pass = boarding_pass.strip()
        row = decode_row(boarding_pass[0:7])
        column = decode_column(boarding_pass[-3:])
        seat = row * 8 + column
        if max < seat:
            max = seat
print(max)
