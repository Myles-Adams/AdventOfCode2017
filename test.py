from anytree import Node
from collections import Counter

n = Node("n", parent=None, weight=20)
a = Node("a", parent=n, weight=20)
b = Node("b", parent=n, weight=20)
c = Node("c", parent=n, weight=10)

my_list = [a,b,c]
new_list = []
for obj in my_list:
    new_list.append(obj.weight)
counter = Counter(new_list)
print(new_list.index(min(counter, key=counter.get)))
