track = []
with open("files/day20.txt", "r") as f:
    for y, line in enumerate(f):
        track.append(["#"] + list(line.split("\n")[0]) + ["#"])
        if "S" in line:
            start = (line.index("S") + 1, y + 1)
        if "E" in line:
            end = (line.index("E") + 1, y + 1)

pad_line = [["#" for _ in range(len(track[0]))]]
track = pad_line + track + pad_line


counter = 0
current_pos = start
while current_pos != end:
    track[current_pos[1]][current_pos[0]] = counter
    if track[current_pos[1] + 1][current_pos[0]] in [".", "E"]:
        current_pos = (current_pos[0], current_pos[1] + 1)
    elif track[current_pos[1] - 1][current_pos[0]] in [".", "E"]:
        current_pos = (current_pos[0], current_pos[1] - 1)
    elif track[current_pos[1]][current_pos[0] + 1] in [".", "E"]:
        current_pos = (current_pos[0] + 1, current_pos[1])
    elif track[current_pos[1]][current_pos[0] - 1] in [".", "E"]:
        current_pos = (current_pos[0] - 1, current_pos[1])
    counter += 1
track[current_pos[1]][current_pos[0]] = counter


MIN_CHEAT = 100
total = 0
for y, line in enumerate(track):
    for x, val in enumerate(line):
        if val != "#" and track[y][x + 1] == "#" and track[y][x + 2] != "#":
            diff = abs(int(val) - int(track[y][x+2])) - 2
            if diff >= MIN_CHEAT:
                total += 1

track = list(zip(*track[::-1]))
for y, line in enumerate(track):
    for x, val in enumerate(line):
        if val != "#" and track[y][x + 1] == "#" and track[y][x + 2] != "#":
            diff = abs(int(val) - int(track[y][x+2])) - 2
            if diff >= MIN_CHEAT:
                total += 1

print(total)



