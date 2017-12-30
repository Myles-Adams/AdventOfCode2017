

f = open("day2.txt", "r")
lines = f.read().splitlines()

total = 0

for lnum in range(0, len(lines)):
    foundNum = False
    nums = list(map(int, lines[lnum].split("\t")))
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            curDiv = nums[i]/nums[j]
            if (curDiv % 1) == 0:
                total += curDiv
                foundNum = True
                break
            curDiv = nums[j]/nums[i]
            if (curDiv % 1) == 0:
                total += curDiv
                foundNum = True
                break
        if foundNum:
            break


print(int(total))

f.close()