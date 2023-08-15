directions_file = '/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/Python/Day-3/arrows.txt'
visited_houses = set()
santa_location = (0, 0)
visited_houses.add(santa_location)
with open(directions_file, 'r') as file:
    for line in file:
        for char in line:
            if char == 'v':
                santa_location = (santa_location[0], santa_location[1] - 1)
            elif char == '>':
                santa_location = (santa_location[0] + 1, santa_location[1])
            elif char == '^':
                santa_location = (santa_location[0], santa_location[1] + 1)
            elif char == '<':
                santa_location = (santa_location[0] - 1, santa_location[1])
            visited_houses.add(santa_location)
print(len(visited_houses))

#PART 2

directions_file = '/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/Python/Day-3/arrows.txt'
visited_houses = set()
santa_location = (0, 0)
robo_santa_location = (0, 0)
visited_houses.add(santa_location)

santa_turn = True
with open(directions_file, 'r') as file:
    for line in file:
        for char in line:
            if santa_turn:
                current_location = santa_location
            else:
                current_location = robo_santa_location

            if char == 'v':
                current_location = (current_location[0], current_location[1] - 1)
            elif char == '>':
                current_location = (current_location[0] + 1, current_location[1])
            elif char == '^':
                current_location = (current_location[0], current_location[1] + 1)
            elif char == '<':
                current_location = (current_location[0] - 1, current_location[1])

            visited_houses.add(current_location)

            if santa_turn:
                santa_location = current_location
            else:
                robo_santa_location = current_location

            santa_turn = not santa_turn

print(len(visited_houses))
