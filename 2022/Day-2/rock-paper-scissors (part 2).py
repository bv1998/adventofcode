def scoremaker(playFile):
    final = 0
    scores = []
    tmp = 0
    with open(playFile, 'r') as file:
        for line in file:
            line = line.strip()
            if line == 'A Y':
                tmp = 4
            elif line == 'B X':
                tmp = 1
            elif line == 'C Y':
                tmp = 6
            elif line == 'C X':
                tmp = 2
            elif line == 'B Z':
                tmp = 9
            elif line == 'A Z':
                tmp = 8
            elif line == 'A X':
                tmp = 3
            elif line == 'C Z':
                tmp = 7
            elif line == 'B Y' or line == 'BY':
                tmp = 5                
            scores.append(tmp)
            final += tmp
            print(tmp)
    print(final)
    return scores

playFile = r'/Users/bryan/Documents/GitHub/adventofcode/2022/Day-2/playbyplay.txt'
plays = scoremaker(playFile)
print(plays[1])