from anytree import Node, RenderTree, AsciiStyle, PreOrderIter
udo = Node("Udo")
marc = Node("Marc")
lian = Node("Lian", parent=marc)
part1 = Node("input part1", parent=marc)
part2 = Node("input part2", parent=marc)

print(RenderTree(udo))
Node('/Udo')
print(RenderTree(marc))

for i in marc.children:
    print(i)
f = Node("f")
b = Node("b", parent=f)
a = Node("a", parent=b)
d = Node("d", parent=b)
c = Node("c", parent=d)
e = Node("e", parent=d)
g = Node("g", parent=f)
i = Node("i", parent=g)
h = Node("h", parent=i)
print(RenderTree(f, style=AsciiStyle()).by_attr())
[node.name for node in PreOrderIter(f)]