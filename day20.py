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


pos_dict = {}
counter = 0
current_pos = start
while current_pos != end:
    track[current_pos[1]][current_pos[0]] = counter
    pos_dict[counter] = current_pos
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
pos_dict[counter] = current_pos


MIN_CHEAT = 100
# Part 01
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


# Part 02
total = 0
for cheat_length in range(MIN_CHEAT, len(pos_dict.keys())):
    for dist in range(cheat_length, len(pos_dict.keys())):
        pos1 = pos_dict[dist]
        pos2 = pos_dict[dist - cheat_length]
        diff = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        if diff <= 20 and cheat_length - diff >= MIN_CHEAT:
            total += 1
print(total)



