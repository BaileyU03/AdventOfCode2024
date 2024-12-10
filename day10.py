def walk(topo, x, y, previous):
    if len(topo[0]) <= x or x < 0 or len(topo) <= y or y < 0:
        return []
    current = topo[y][x]
    if previous + 1 != current:
        return []
    if current == 9:
        return [[x,y]]
    return walk(topo, x + 1, y, current) + walk(topo, x - 1, y, current) + walk(topo, x, y + 1, current) + walk(topo, x, y - 1, current)


topo_map = []
zero_points = []
with open("files/day10.txt", "r") as f:
    for y, line in enumerate(f):
        topo_map.append(list(map(int, list(line.split("\n")[0]))))
        for x, char in enumerate(line):
            if char == "0":
                zero_points.append([x, y])


total = 0
for z in zero_points:
    nine_points = walk(topo_map, z[0], z[1], -1)
    total += len([list(t) for t in set(tuple(element) for element in nine_points)])
print(total)
