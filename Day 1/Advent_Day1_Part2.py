def solvedayone_part2(input):
    total = 0
    input_s = str(input)
    length = len(input)
    for i in range(0, len(input_s)):
        h_index = int((i + length/2) % length)
        if input_s[i] == input_s[h_index]:
            total += int(input_s[i])
    print(total)


f = open("Day1.txt", "r")
input = f.readline().rstrip("\n")


solvedayone_part2(input)