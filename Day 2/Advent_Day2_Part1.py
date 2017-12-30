

f = open("day2.txt", "r")
total = 0
curMax = 0
curMin = 0

for line in f.readlines():
    allLines = line.split("\t")
    allNums = list(map(int, allLines))
    curMax = max(allNums)
    curMin = min(allNums)
    total += (int(curMax) - int(curMin))

print(total)

f.close()