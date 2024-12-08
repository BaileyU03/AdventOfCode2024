nodes = {}
width = 0
height = 0

with open("files/day08.txt", "r") as f:
    for y, line in enumerate(f):
        height += 1
        clean_line = line.split("\n")[0]
        width = len(line)
        for x, char in enumerate(clean_line):
            if char != ".":
                if char in nodes.keys():
                    nodes[char].append([x, y])
                else:
                    nodes[char] = [[x, y]]

antinodes = []
for node in nodes.values():
    for i in range(len(node)):
        for j in range(i + 1, len(node)):
            pos_i, pos_j = node[i], node[j]
            diff = [pos_i[0]-pos_j[0], pos_i[1]-pos_j[1]]
            antinode1, antinode2 = [pos_i[0]+diff[0], pos_i[1]+diff[1]], [pos_j[0]-diff[0], pos_j[1]-diff[1]]
            if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height and antinode1[:] not in antinodes:
                antinodes.append(antinode1)
            if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height and antinode2[:] not in antinodes:
                antinodes.append(antinode2)

print(len(antinodes))
