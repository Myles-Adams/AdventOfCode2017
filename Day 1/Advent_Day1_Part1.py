def solvedayone_part1(input):
    total = 0
    input_s = str(input)
    for i in range(-1, len(input_s) - 1):
        if input_s[i] == input_s[i+1]:
            total += int(input_s[i])
    print(total)


f = open("Day1.txt", "r")
input = f.readline().rstrip("\n")

solvedayone_part1(input)