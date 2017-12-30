f = open('day6.txt', 'r')
banksInput = f.read().rstrip('\n')

allConfigs = []
sBanks = banksInput.split("\t")
banks = list(map(int, sBanks))
numBanks = len(banks)

while banks not in allConfigs:
    allConfigs.append(list(banks))
    maxIndex = banks.index(max(banks))
    blocks = banks[maxIndex]
    banks[maxIndex] = 0

    ndx = (maxIndex + 1) % numBanks
    while blocks > 0:
        banks[ndx] += 1
        blocks -= 1
        ndx = (ndx + 1) % numBanks

targetBanks = list(banks)
numCycles = 0

while True:
    maxIndex = banks.index(max(banks))
    blocks = banks[maxIndex]
    banks[maxIndex] = 0

    ndx = (maxIndex + 1) % numBanks
    while blocks > 0:
        banks[ndx] += 1
        blocks -= 1
        ndx = (ndx + 1) % numBanks

    numCycles += 1
    if banks == targetBanks:
        break

print(numCycles)

