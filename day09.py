with open("files/day09.txt", "r") as f:
    disk_map = list(map(int, list(f.readline())))

disk = []
counter = 0
gap_finder = []
file_data = []
for i, x in enumerate(disk_map):
    if i % 2 == 0:
        if x > 0:
            file_data.append({"pos": len(disk), "size": x, "value": counter})
        disk += [counter for _ in range(x)]
    else:
        if x > 0:
            gap_finder.append({"pos": len(disk), "size": x})
        disk += [-1 for _ in range(x)]
        counter += 1


# Part 1
new_disk = disk[:]
num_of_blanks = sum([e for i, e in enumerate(disk_map) if i % 2 == 1])
while num_of_blanks > 0:
    new_disk[new_disk.index(-1)] = new_disk[-1]
    new_disk = new_disk[:-1]
    num_of_blanks -= 1

checksum = 0
for i, x in enumerate(new_disk):
    checksum += i * x
print(checksum)


# Part 2
file_data.reverse()
for file in file_data:
    for gap in gap_finder:
        if gap["pos"] > file["pos"]:
            break
        if gap["size"] >= file["size"]:
            for i in range(file["size"]):
                disk[gap["pos"] + i] = file["value"]
                disk[file["pos"] + i] = -1
            gap["size"] -= file["size"]
            gap["pos"] += file["size"]
            break

checksum = 0
for i, x in enumerate(disk):
    if x >= 0:
        checksum += i * x
print(checksum)
