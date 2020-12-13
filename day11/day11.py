
def get_pos(seats, x, y):
    if x >= len(seats) or x < 0:
        return "|"
    row = seats[x]
    if y >= len(row) or y < 0:
        return "|"
    return row[y]

def number_occupied_arround(seats, x, y):
    arounds = [
        (0, -1), (0, +1), # left / right
        (+1, 0), (-1, 0), # top / bottom
        (+1, +1), (+1, -1),
        (-1, -1), (-1, +1)
    ]
    neighbours = []
    for around in arounds:
        neighbours.append(get_pos(seats, x + around[0], y + around[1]))
    return neighbours.count("#")

def calc_round(seats):
    new_seats = []
    for x, row in enumerate(seats):
        new_row = ""
        for y, actual in enumerate(row):
            occupied = number_occupied_arround(seats, x, y)
            if actual == "L":
                if occupied == 0:
                    new_row += "#"
                else:
                    new_row += "L"
            elif actual == "#":
                if occupied >= 4:
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

while True:
    new_seats = calc_round(seats)
    if seats == new_seats:
        break
    seats = new_seats

occupied = sum([row.count("#") for row in seats])
print(occupied)
