WIDTH = 71
FALLEN_BITS = 1024


def search(space):
    all_vertices = []
    for y, line in enumerate(space):
        for x, val in enumerate(line):
            if x == 0 and y == 0:
                all_vertices.append({"pos": (0, 0), "dist": 0, "prev": ()})
            elif val == ".":
                all_vertices.append({"pos": (x, y), "dist": float("inf"), "prev": ()})

    vertices = all_vertices[:]
    while len(vertices) > 0:
        dists = [v['dist'] for v in vertices]
        u = vertices[min(range(len(dists)), key=dists.__getitem__)]
        vertices.remove(u)
        poss = [v["pos"] for v in vertices]
        # Right
        if (u["pos"][0] + 1, u["pos"][1]) in poss:
            v = vertices[poss.index((u["pos"][0] + 1, u["pos"][1]))]
            alt = u["dist"] + 1
            if alt < v["dist"]:
                v["dist"] = alt
                v["prev"] = u["pos"]
        # Left
        if (u["pos"][0] - 1, u["pos"][1]) in poss:
            v = vertices[poss.index((u["pos"][0] - 1, u["pos"][1]))]
            alt = u["dist"] + 1
            if alt < v["dist"]:
                v["dist"] = alt
                v["prev"] = u["pos"]
        # Up
        if (u["pos"][0], u["pos"][1] - 1) in poss:
            v = vertices[poss.index((u["pos"][0], u["pos"][1] - 1))]
            alt = u["dist"] + 1
            if alt < v["dist"]:
                v["dist"] = alt
                v["prev"] = u["pos"]
        # Down
        if (u["pos"][0], u["pos"][1] + 1) in poss:
            v = vertices[poss.index((u["pos"][0], u["pos"][1] + 1))]
            alt = u["dist"] + 1
            if alt < v["dist"]:
                v["dist"] = alt
                v["prev"] = u["pos"]
    return all_vertices


spaces = [[["." for _ in range(WIDTH)] for _ in range(WIDTH)]]
bytes = []
with open("files/day18.txt", "r") as f:
    for i, line in enumerate(f):
        bytes.append(line.split("\n")[0])
        coords = list(map(int, line.split("\n")[0].split(",")))
        new_space = [x[:] for x in spaces[-1]]
        new_space[coords[1]][coords[0]] = "#"
        spaces.append(new_space)

# Part 01
space = spaces[FALLEN_BITS][:]
all_vertices = search(space)
print([v["dist"] for v in all_vertices if v["pos"] == (WIDTH - 1, WIDTH - 1)][0])

# Part 02
min_pointer = 0
max_pointer = len(spaces)
best = 0
while min_pointer <= max_pointer:
    space_pointer = min_pointer + (max_pointer - min_pointer) // 2
    space = spaces[space_pointer]
    all_vertices = search(space)
    distance_to_end = [v["dist"] for v in all_vertices if v["pos"] == (WIDTH - 1, WIDTH - 1)][0]
    if distance_to_end == float("inf"):
        max_pointer = space_pointer - 1
    else:
        best = space_pointer
        min_pointer = space_pointer + 1

print(bytes[best])
