textFile = r'/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/Python/Day-1/steps.txt'
i = 0
x = 0
with open(textFile, 'r') as file:
    for line in file: 
        for char in line:
            if char == '(': i = i + 1
            else: i = i - 1
            x+=1
            if i < 0 : print(x)
print(i)
