with open("files/day09.txt", "r") as f:
    disk_map = list(map(int, list(f.readline())))


disk = []
counter = 0
for i, x in enumerate(disk_map):
    if i % 2 == 0:
        disk += [counter for _ in range(x)]
    else:
        disk += [-1 for _ in range(x)]
        counter += 1


num_of_blanks = sum([e for i, e in enumerate(disk_map) if i % 2 == 1])
while num_of_blanks > 0:
    disk[disk.index(-1)] = disk[-1]
    disk = disk[:-1]
    num_of_blanks -= 1


checksum = 0
for i, x in enumerate(disk):
    checksum += i * x


print(checksum)
