def calculate_win(move):
    match move:
        case 'rock':
            return 8
        case 'paper':
            return 9
        case 'scissors':
            return 7


def calculate_loss(move):
    match move:
        case 'rock':
            return 3
        case 'paper':
            return 1
        case 'scissors':
            return 2


def calculate_draw(move):
    match move:
        case 'rock':
            return 4
        case 'paper':
            return 5
        case 'scissors':
            return 6


file = open('input', 'r')
lines = file.readlines()
score = 0

for line in lines:
    clean = line.replace('\n', '')
    moves = clean.split(" ")
    theirs = moves[0]
    ours = moves[1]

    match theirs:
        case "A":
            theirs = 'rock'
        case "B":
            theirs = 'paper'
        case "C":
            theirs = 'scissors'

    match ours:
        case "X":
            score += calculate_loss(theirs)
        case "Y":
            score += calculate_draw(theirs)
        case "Z":
            score += calculate_win(theirs)

print(score)
