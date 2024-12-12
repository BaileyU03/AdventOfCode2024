def search(x, y, char):
    perimeter = 0
    area = 0
    queue = [{"x": x, "y": y}]
    garden[y][x]["visited"] = True
    while len(queue) > 0:
        pos = queue.pop(0)
        area += 1
        # Up
        if pos["y"] == 0 or garden[pos["y"] - 1][pos["x"]]["ID"] != char:
            perimeter += 1
        elif not garden[pos["y"] - 1][pos["x"]]["visited"]:
            garden[pos["y"] - 1][pos["x"]]["visited"] = True
            queue.append({"x": pos["x"], "y": pos["y"] - 1})
        # Down
        if pos["y"] + 1 == len(garden) or garden[pos["y"] + 1][pos["x"]]["ID"] != char:
            perimeter += 1
        elif not garden[pos["y"] + 1][pos["x"]]["visited"]:
            garden[pos["y"] + 1][pos["x"]]["visited"] = True
            queue.append({"x": pos["x"], "y": pos["y"] + 1})
        # Left
        if pos["x"] == 0 or garden[pos["y"]][pos["x"]-1]["ID"] != char:
            perimeter += 1
        elif not garden[pos["y"]][pos["x"]-1]["visited"]:
            garden[pos["y"]][pos["x"] - 1]["visited"] = True
            queue.append({"x": pos["x"]-1, "y": pos["y"]})
        # Right
        if pos["x"] + 1 == len(garden[0]) or garden[pos["y"]][pos["x"]+1]["ID"] != char:
            perimeter += 1
        elif not garden[pos["y"]][pos["x"]+1]["visited"]:
            garden[pos["y"]][pos["x"] + 1]["visited"] = True
            queue.append({"x": pos["x"]+1, "y": pos["y"]})
    return perimeter * area


garden = []
with open("files/day12.txt", "r") as f:
    for line in f:
        garden.append([{"ID": x, "visited": False} for x in line.split("\n")[0]])

total = 0
for y, line in enumerate(garden):
    for x, char in enumerate(line):
        if not char["visited"]:
            total += search(x, y, char["ID"])
print(total)
