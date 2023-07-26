wrapFile = r'/Users/bryan/Desktop/Python_scripts/Advent-of-Code-2015/PHP/Day-2/wrapFile.txt'
with open(wrapFile, 'r') as file:
    i=0
    for line in file: 
        nums = line.split('x')
        l = int(nums[0])
        w = int(nums[1])
        h = int(nums[2])
        i += (2*l*w + 2*w*h + 2*h*l)+ (min(l*w, w*h, h*l))
print(i)