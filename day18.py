WIDTH = 71
FALLEN_BITS = 1024
space = [["." for _ in range(WIDTH)] for _ in range(WIDTH)]
with open("files/day18.txt", "r") as f:
    for i, line in enumerate(f):
        if i == FALLEN_BITS:
            break
        coords = list(map(int, line.split("\n")[0].split(",")))
        space[coords[1]][coords[0]] = "#"


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


print([v["dist"] for v in all_vertices if v["pos"] == (WIDTH - 1, WIDTH - 1)][0])
