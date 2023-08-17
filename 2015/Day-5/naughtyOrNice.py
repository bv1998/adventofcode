myFile = "/Users/bryan/Documents/GitHub/adventofcode/2015/Day-5/list.txt"
nice = 0
naughty = 0
check = False
with open(myFile, 'r') as file:
    vowelCount = 0
    with open(myFile, 'r') as file:
        for line in file:
            vowelCount = sum(1 for char in line if char in "aeiou")
            check = False
            repeated_pair = False
            if vowelCount >= 3:
                check = True
            for i in range(len(line) - 1):
                if line[i] == line[i + 1]:
                    repeated_pair = True
                    break
            if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
                check = False
            if repeated_pair and check:
                nice += 1
            else:
                naughty += 1
    print(nice, naughty)
