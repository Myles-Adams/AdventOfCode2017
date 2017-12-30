f = open("day5.txt", "r")

fileLines = f.read().splitlines()
instructions = list(map(int, fileLines))
numSteps = 0
ndx = 0;

while ndx < len(instructions):
    tempNdx = ndx
    ndx += instructions[ndx]
    if instructions[tempNdx] >= 3:
        instructions[tempNdx] -= 1
    else:
        instructions[tempNdx] += 1
    numSteps += 1

print(numSteps)
