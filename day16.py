maze = []
with open("files/day16.txt", "r") as f:
    for y, line in enumerate(f):
        ll = list(line.split("\n")[0])
        maze.append(ll)


all_vertices = []
for y, line in enumerate(maze):
    for x, val in enumerate(line):
        if val == ".":
            all_vertices.append({"pos": (x, y), "dist": float("inf"), "prev": (), "dir": (), "type": 0})
        elif val == "S":
            all_vertices.append({"pos": (x, y), "dist": 0, "prev": (), "dir": (1, 0), "type": 1})
        elif val == "E":
            all_vertices.append({"pos": (x, y), "dist": float("inf"), "prev": (), "dir": (), "type": 2})


vertices = all_vertices[:]
while len(vertices) > 0:
    dists = [v['dist'] for v in vertices]
    u = vertices[min(range(len(dists)), key=dists.__getitem__)]
    vertices.remove(u)
    poss = [v["pos"] for v in vertices]
    # Right
    if (u["pos"][0] + 1, u["pos"][1]) in poss:
        v = vertices[poss.index((u["pos"][0] + 1, u["pos"][1]))]
        alt = u["dist"] + 1 if u["dir"] == (1, 0) else u["dist"] + 1001
        if alt < v["dist"]:
            v["dist"] = alt
            v["prev"] = u["pos"]
            v["dir"] = (1, 0)
    # Left
    if (u["pos"][0] - 1, u["pos"][1]) in poss:
        v = vertices[poss.index((u["pos"][0] - 1, u["pos"][1]))]
        alt = u["dist"] + 1 if u["dir"] == (-1, 0) else u["dist"] + 1001
        if alt < v["dist"]:
            v["dist"] = alt
            v["prev"] = u["pos"]
            v["dir"] = (-1, 0)
    # Up
    if (u["pos"][0], u["pos"][1] - 1) in poss:
        v = vertices[poss.index((u["pos"][0], u["pos"][1] - 1))]
        alt = u["dist"] + 1 if u["dir"] == (0, -1) else u["dist"] + 1001
        if alt < v["dist"]:
            v["dist"] = alt
            v["prev"] = u["pos"]
            v["dir"] = (0, -1)
    # Down
    if (u["pos"][0], u["pos"][1] + 1) in poss:
        v = vertices[poss.index((u["pos"][0], u["pos"][1] + 1))]
        alt = u["dist"] + 1 if u["dir"] == (0, 1) else u["dist"] + 1001
        if alt < v["dist"]:
            v["dist"] = alt
            v["prev"] = u["pos"]
            v["dir"] = (0, 1)


print([v["dist"] for v in all_vertices if v["type"] == 2][0])
