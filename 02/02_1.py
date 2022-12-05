file = open('input', 'r')
lines = file.readlines()

score = 0

for line in lines:
    clean = line.replace('\n', '')
    moves = clean.split(" ")
    theirs = moves[0]
    ours = moves[1]

    # calculate points for our move
    match ours:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3

    # see who won
    match theirs:
        case "A":
            if ours == "X":
                score += 3
            if ours == "Y":
                score += 6
            if ours == "Z":
                score += 0
        case "B":
            if ours == "X":
                score += 0
            if ours == "Y":
                score += 3
            if ours == "Z":
                score += 6
        case "C":
            if ours == "X":
                score += 6
            if ours == "Y":
                score += 0
            if ours == "Z":
                score += 3

print(score)