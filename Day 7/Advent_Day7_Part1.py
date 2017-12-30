f = open("day7.txt", "r")

fileLines = f.read().splitlines()
d = {}

for i in range(0, len(fileLines)):
    lineSplit = fileLines[i].split(" ")

    if len(lineSplit) > 2:
        if lineSplit[0] not in d:
            d[lineSplit[0]] = " "
        for j in range(3, len(lineSplit)):
            if j != len(lineSplit) - 1:
                lineSplit[j] = lineSplit[j][:-1]
            d[lineSplit[j]] = lineSplit[0]
    else:
        if lineSplit[0] not in d:
            d[lineSplit[0]] = " "

for key, value in d.items():
    if value == " ":
        print(key)

