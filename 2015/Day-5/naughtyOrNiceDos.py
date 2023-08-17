myFile = "/Users/bryan/Documents/GitHub/adventofcode/2015/Day-5/list.txt"
nice = 0
with open(myFile, 'r') as file:
    for line in file:
        has_repeated_pair = False
        has_repeating_letter = False
        for i in range(len(line) - 2):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                has_repeated_pair = True
                break
        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                has_repeating_letter = True
                break
        if has_repeated_pair and has_repeating_letter:
            nice += 1

print(nice)
