from hmac import new
from tokenize import group

i = []
txtFile = '/Users/bryan/Desktop/Python_scripts/elf-numbers-day-1'

def read_numbers_from_file(txtFile):
    groups = []
    current_group = []
    
    with open(txtFile, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                current_group.append(line)
            else:
                if current_group:
                    groups.append(','.join(current_group))
                    current_group = []
    
    if current_group:
        groups.append(','.join(current_group))
    
    return groups



number_groups = read_numbers_from_file(txtFile)
for d in number_groups:
    x = d.split(",")
    numbers_as_integers = [int(num) for num in x]
    total_sum = sum(numbers_as_integers)
    i.append(total_sum)
maxNum = max(i)
positionNum = i.index(maxNum) + 1

print("Wow this is awesome! The elf with the most is Elf number {} and his total is {} ".format(positionNum, maxNum))

print("Oh no you need the top 3?")

i.sort(reverse=True)
newMax = int(i[0])+ int(i[1])+ int(i[2])

print("That new number is {}".format(newMax))

    