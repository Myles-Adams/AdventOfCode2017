
def find_steps(num):
    middles = [1, 1, 1, 1]
    i = 0
    square = 0

    if num == 1:
        return 0

    while square < num:
        i += 1
        square = (2*i + 1)**2

    for ndx in range(0,4):
        for j in range(0, i):
            middles[ndx] += (ndx*2 + 1) + 8*j

    for ndx in range(0,4):
        if middles[ndx] == num:
            return i
        elif num <= middles[ndx] + i:
            for j in range (0, i+1):
                if middles[ndx] + j == num:
                    return i+j
        elif num >= middles[ndx] - i:
            for j in range (0, i+1):
                if middles[ndx] - j == num:
                    return i+j


print(find_steps(347991))





