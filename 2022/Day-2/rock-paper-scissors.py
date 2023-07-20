def scoremaker(playFile):
    final = 0
    scores = []
    tmp = 0
    with open(playFile, 'r') as file:
        for line in file:
            line = line.strip()
            if line == 'AY':
                tmp = 8
            elif line == 'BX':
                tmp = 1
            elif line == 'CY':
                tmp = 2
            elif line == 'CX':
                tmp = 7
            elif line == 'BZ':
                tmp = 9
            elif line == 'AZ':
                tmp = 3
            else:
                tmp = 3
            scores.append(tmp)
            final += tmp
    print(final)
    return scores

playFile = "K:\Development Folder\Advent of code 2022\playbyplay.txt"
plays = scoremaker(playFile)
