import string

count = list(string.ascii_letters)
num = 0
Inventory = r'C:\Users\bryan\Documents\GitHub\adventofcode\2022\Day-3\inventory.txt'

def getLet(bag):
    stringLen = len(bag)
    tmp = bag[0:stringLen//2]
    tmpDos = bag[stringLen//2:]
    return getMatchingItems(tmp, tmpDos)

def getMatchingItems(tmp, tmpDos):
    return [item for item in tmp if item in tmpDos]

def getVal(let):
    return count.index(let)

with open(Inventory, 'r') as file:
    for line in file:
        test = list(line.strip())
        test = getLet(test)
        for character in test:
            num += getVal(character)

print(num)

