robots = []
with open("files/day14.txt", "r") as f:
    for line in f:
        split_l = line.split("\n")[0].split()
        p = list(map(int, split_l[0][2:].split(",")))
        v = list(map(int, split_l[1][2:].split(",")))
        robots.append([p, v])


WIDTH = 101
HEIGHT = 103
bathroom = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for robot in robots:
    pos = robot[0]
    vel = robot[1]
    for _ in range(100):
        pos = [(pos[0] + vel[0]) % WIDTH,
               (pos[1] + vel[1]) % HEIGHT]
    bathroom[pos[1]][pos[0]] += 1


quadrant_sums = [0, 0,
                 0, 0]
for y, line in enumerate(bathroom):
    for x, val in enumerate(line):
        if val == 0:
            continue
        if y < HEIGHT // 2 and x < WIDTH // 2:
            quadrant_sums[0] += val
        if y < HEIGHT // 2 and x > WIDTH // 2:
            quadrant_sums[1] += val
        if y > HEIGHT // 2 and x < WIDTH // 2:
            quadrant_sums[2] += val
        if y > HEIGHT // 2 and x > WIDTH // 2:
            quadrant_sums[3] += val


total = 1
for q in quadrant_sums:
    total *= q
print(total)
