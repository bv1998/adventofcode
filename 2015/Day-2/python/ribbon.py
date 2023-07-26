wrapFile = r'/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/PHP/Day-2/wrapFile.txt'
with open(wrapFile, 'r') as file:
    i = 0
    for line in file:
        nums = line.split('x')
        nums = sorted(nums, key=int)
        l = int(nums[0])
        m = int(nums[1])
        z = int(nums[2])
        i += (l + l + m + m) + (l * m * z)

print(i)
