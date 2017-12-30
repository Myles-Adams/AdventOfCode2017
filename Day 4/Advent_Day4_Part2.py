from collections import defaultdict

f = open("day4.txt", "r")
all_lines = f.read().splitlines()
num_valid = 0
isValid = True

for line in all_lines:
    d = defaultdict(list)
    isValid = True
    split_line = line.split(" ")
    for word in split_line:
        w_len = len(word)
        d[w_len].append(word)

    for key, value in d.items():
        for i in range(0, len(value)):
            value[i] = ''.join(sorted(value[i]))

        for i in range(0, len(value) - 1):
            for j in range(i+1, len(value)):
                if value[i] == value[j]:
                    isValid = False
                    break
            if not isValid:
                break

        if not isValid:
            break

    if isValid:
        num_valid += 1

print(num_valid)


