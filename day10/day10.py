
with open('input.txt') as file:
    adapters = [int(x) for x in file.read().splitlines()]

adapters.sort()
adapters.append(adapters[-1]+3)
last = 0
diffs = {}
diffs_sequence = []
for jolt in adapters:
    diff = jolt - last
    diffs_sequence.append(diff)
    if diff not in diffs:
        diffs[diff] = 0
    diffs[diff] += 1
    last = jolt
print(diffs[1] * diffs[3])

# Help was needed: https://www.reddit.com/r/adventofcode/comments/kbv1y8/2020_day_10_help_with_part_2/

sequences = []
sequence = 0

for diff in diffs_sequence:
    if diff == 3:
        if sequence:
            sequences.append(sequence)
        sequence = 0
    else:
        sequence += 1

mult = 1
for seq in sequences:
    if seq == 2:
        mult *= 2
    elif seq == 3:
        mult *= 4
    elif seq == 4:
        mult *= 7

print(mult)
