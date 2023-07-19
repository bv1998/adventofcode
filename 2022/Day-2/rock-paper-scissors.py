plays =[]
final = 0
playFile = ""

def scoremaker(playFile):
     
    scores=[]
    tmp = 0
    with open(playFile, 'r') as file:
        for line in file:
            line = line.strip()
            if line == 'A Y':
                tmp = 8
            elif line ==' B X':
                tmp = 1
            elif line == 'C Y':
                tmp = 2
            elif line == 'C X':
                tmp = 7
            elif line == 'B Z':
                tmp = 9
            elif line == 'A Z':
                tmp = 3
            else:
                tmp = 6
        scores.append(tmp)
    return scores
plays = scoremaker('playbyplay.txt')

for i in range(0, len(arr)):    
   final = final + arr[i];  

print(final)
            