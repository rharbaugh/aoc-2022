with open('input') as f:
    lines = f.read().splitlines()

elves = []
calories = 0

for line in lines:
    if line.isdigit():
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0

elves.sort(reverse=True)
print(sum(elves[0:3]))
