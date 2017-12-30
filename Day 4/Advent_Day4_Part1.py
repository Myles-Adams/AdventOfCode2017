f = open("day4.txt", "r")
numValid = 0

for line in f.readlines():
    line = line[:-1]
    isValid = True
    d = {}
    words = line.split(" ")
    for i in range(0, len(words)):
        if words[i] in d:
            isValid = False
            break
        else:
            d[words[i]] = ''

    if isValid:
        numValid += 1

print(numValid)
