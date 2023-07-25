# import string

# count = list(string.ascii_letters)
# num = 0
# Inventory = r'/Users/bryan/Documents/GitHub/adventofcode/2022/Day-3/inventory.txt'

# def getLet(bag):
#     stringLen = len(bag)
#     tmp = bag[0:stringLen//2]
#     tmpDos = bag[stringLen//2:]
#     return getMatchingItems(tmp, tmpDos)

# def getMatchingItems(tmp, tmpDos):
#     return [item for item in tmp if item in tmpDos]

# def getVal(let):
#     return count.index(let)

# with open(Inventory, 'r') as file:
#     for line in file:
#         test = list(line.strip())
#         test = getLet(test)
#         for character in test:
#             num += getVal(character) + 1

# print(num)

def calculate_priority(item_type):
    if 'a' <= item_type <= 'z':
        return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z':
        return ord(item_type) - ord('A') + 27
    else:
        raise ValueError("Invalid item type")

def find_common_items(rucksack_contents):
    common_items = []
    for rucksack in rucksack_contents:
        compartment1 = rucksack[:len(rucksack) // 2]
        compartment2 = rucksack[len(rucksack) // 2:]
        for item_type in compartment1:
            if item_type in compartment2 and item_type not in common_items:
                common_items.append(item_type)
    return common_items

def calculate_total_priority(common_items):
    return sum(calculate_priority(item_type) for item_type in common_items)

# Sample input
rucksack_contents = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

common_items = find_common_items(rucksack_contents)
total_priority = calculate_total_priority(common_items)

print("Common Items:", common_items)
print("Total Priority:", total_priority)
