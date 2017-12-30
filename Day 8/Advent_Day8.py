f = open("day8.txt", "r")
lines = f.read().splitlines()
d = {}

for ndx in range (0, len(lines)):
    curLine = lines[ndx].split(" ")
    if curLine[0] not in d:
        d[curLine[0]] = 0
    if curLine[4] not in d:
        d[curLine[4]] = 0

    if curLine[5] == ">":
        if d[curLine[4]] > int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

    elif curLine[5] == "<":
        if d[curLine[4]] < int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

    elif curLine[5] == ">=":
        if d[curLine[4]] >= int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

    elif curLine[5] == "<=":
        if d[curLine[4]] <= int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

    elif curLine[5] == "==":
        if d[curLine[4]] == int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

    elif curLine[5] == "!=":
        if d[curLine[4]] != int(curLine[6]):
            if curLine[1] == "inc":
                d[curLine[0]] += int(curLine[2])
            else:
                d[curLine[0]] -= int(curLine[2])

maxValue = 0
for key, value in d.items():
    if value > maxValue:
        maxValue = value

print(maxValue)