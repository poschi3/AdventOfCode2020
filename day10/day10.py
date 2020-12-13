
with open('input.txt') as file:
    adapters = [int(x) for x in file.read().splitlines()]

adapters.sort()
adapters.append(adapters[-1]+3)
last = 0
diffs = {}
for jolt in adapters:
    diff = jolt - last
    if diff not in diffs:
        diffs[diff] = 0
    diffs[diff] += 1
    last = jolt

print(diffs[1] * diffs[3])
