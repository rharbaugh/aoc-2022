file = open('input', 'r')
lines = file.readlines()


def get_char_priority(char):
    value = ord(char)
    if value < 97:
        return value - 64 + 26
    else:
        return value - 96

priority_sum = 0

for line in lines:
    clean = line.replace('\n', '')
    length = len(clean)
    first = clean[0:int(length/2)]
    second = clean[-int(length/2):]
    match = ''.join(set(first).intersection(second))
    match_value = get_char_priority(match)
    priority_sum += match_value

print(priority_sum)

# PART 2
badge_type_priority_sum = 0

for x in range(0, len(lines), 3):
    first = lines[x].replace('\n', '')
    second = lines[x+1].replace('\n', '')
    third = lines[x+2].replace('\n', '')

    badge_type = ''.join(set(first).intersection(second).intersection(third))
    badge_type_priority = get_char_priority(badge_type)
    badge_type_priority_sum += badge_type_priority

print(badge_type_priority_sum)