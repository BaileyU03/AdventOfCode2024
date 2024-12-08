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


antinodes1 = []
antinodes2 = []
for node in nodes.values():
    for i in range(len(node)):
        for j in range(i + 1, len(node)):
            # Part 1
            pos_i, pos_j = node[i], node[j]
            diff = [pos_i[0]-pos_j[0], pos_i[1]-pos_j[1]]
            antinode1, antinode2 = [pos_i[0]+diff[0], pos_i[1]+diff[1]], [pos_j[0]-diff[0], pos_j[1]-diff[1]]
            if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height and antinode1[:] not in antinodes1:
                antinodes1.append(antinode1)
            if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height and antinode2[:] not in antinodes1:
                antinodes1.append(antinode2)
            # Part 2
            part2diff = diff[:]
            if pos_i[:] not in antinodes2:
                antinodes2.append(pos_i)
            if pos_j[:] not in antinodes2:
                antinodes2.append(pos_j)
            while 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                if antinode1[:] not in antinodes2:
                    antinodes2.append(antinode1)
                part2diff = [sum(x) for x in zip(part2diff, diff)]
                antinode1 = [pos_i[0] + part2diff[0], pos_i[1] + part2diff[1]]
            part2diff = diff[:]
            while 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                if antinode2[:] not in antinodes2:
                    antinodes2.append(antinode2)
                part2diff = [sum(x) for x in zip(part2diff, diff)]
                antinode2 = [pos_j[0]-part2diff[0], pos_j[1]-part2diff[1]]


print(len(antinodes1))
print(len(antinodes2))
