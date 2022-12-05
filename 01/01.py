file = open('input', 'r')
lines = file.readlines()

elves = []
calories = 0

for line in lines:
    clean = line.replace('\n', '')
    if clean.isdigit():
        calories += int(clean)
    else:
        elves.append(calories)
        calories = 0

elves.sort(reverse=True)
print(sum(elves[0:3]))