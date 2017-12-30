from anytree import Node
import re

def getWeight(root):
    if root.children == None:
        return root.weight
    child_total = 0
    for child in root.children:
        child_total += getWeight(child)
    return (child_total + root.weight)


def checkBalance(root):
    if root.children == None:
        return 0
    rootWeight = getWeight(root)
    numChildren = len(root.children)
    for child in root.children:
        child_t_weight = rootWeight/numChildren
        child_weight = getWeight(child)
        if child_weight != child_t_weight:
            delta = child_t_weight - child_weight
            retVal = child_weight + delta
            return retVal


f = open("test7.txt", "r")

fileLines = f.read().splitlines()
d = {}

for line in fileLines:
    lineSplit = line.split(" ")

    if len(lineSplit) > 2:
        if lineSplit[0] not in d:
            d[lineSplit[0]] = Node(lineSplit[0], weight=int(re.search('\(([^)]+)', lineSplit[1]).group(1)), parent=None)
        else:
            d[lineSplit[0]].weight = int(re.search('\(([^)]+)', lineSplit[1]).group(1))
        for j in range(3, len(lineSplit)):
            if j != len(lineSplit) - 1:
                lineSplit[j] = lineSplit[j][:-1]
            if lineSplit[j] not in d:
                d[lineSplit[j]] = Node(lineSplit[j], weight=None, parent=d[lineSplit[0]])
            else:
                d[lineSplit[j]].parent = d[lineSplit[0]]
    else:
        if lineSplit[0] not in d:
            d[lineSplit[0]] = Node(lineSplit[0], weight=int(re.search('\(([^)]+)', lineSplit[1]).group(1)), parent=None)
        else:
            d[lineSplit[0]].weight = int(re.search('\(([^)]+)', lineSplit[1]).group(1))

new_weight = 0
for key, value in d.items():
    root_weight = getWeight(value)
    num_children = len(value.children)

    weights = []
    for child in value.children:
        weight.append()



    for child in value.children:
        child_weight = getWeight(child)

        for node in value.children
        child_target_weight = (root_weight - value.weight)/num_children
        if child_weight != child_target_weight:
            # new_weight = child_weight + (child_target_weight - child_weight)
            new_weight = child_target_weight
        if new_weight != 0:
            break
    if new_weight != 0:
        break

print(new_weight)