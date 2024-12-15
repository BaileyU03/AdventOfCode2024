def get_direction(arrow):
    if arrow == "^":
        return [0, -1]
    if arrow == "v":
        return [0, 1]
    if arrow == "<":
        return [-1, 0]
    if arrow == ">":
        return [1, 0]


def move(direction, pos):
    return [pos[0] + direction[0], pos[1] + direction[1]]


warehouse = []
steps = ""
with open("files/day15.txt", "r") as f:
    warehouse_mode = True
    for y, line in enumerate(f):
        if line == "\n":
            warehouse_mode = False
            continue
        if warehouse_mode:
            warehouse.append(list(line.split("\n")[0]))
            if "@" in line:
                pos = [list(line).index("@"), y]
        else:
            steps += line.split("\n")[0]
warehouse[pos[1]][pos[0]] = "."


for step in steps:
    direction = get_direction(step)
    looking = move(direction, pos[:])
    adj = looking[:]
    boxes = False
    while warehouse[looking[1]][looking[0]] == "O":
        boxes = True
        looking = move(direction, looking)
    if warehouse[looking[1]][looking[0]] == ".":
        if boxes:
            warehouse[looking[1]][looking[0]] = "O"
            warehouse[adj[1]][adj[0]] = "."
        pos = adj[:]


total = 0
for y, line in enumerate(warehouse):
    for x, char in enumerate(line):
        if char == "O":
            total += 100*y + x

print(total)


