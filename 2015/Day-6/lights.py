instructionstext = '/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/Python/coordinate-instructions.txt'
import numpy as np
grid = np.zeros((1000,1000), dtype=int)

with open(instructionstext, 'r') as file:
    for line in file:
        words = line.split()
        if words[0] == 'toggle':
            sy, sx = map(int, words[1].split(','))
            ex, ey = map(int, words[3].split(','))
            grid[sx:ex+1, sy:ey+1] += 2 
        else:
            sy, sx = map(int, words[2].split(','))
            ex, ey = map(int, words[4].split(','))
            if (words[1] == 'on'):
                grid[sx:ex+1, sy:ey+1] += 1 
            else:
                grid[sx:ex+1, sy:ey+1] += 0 
        
lit_lights = np.sum(grid)
print("Number of lit lights:", lit_lights)
