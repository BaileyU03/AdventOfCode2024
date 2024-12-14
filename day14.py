from matplotlib import pyplot as plt


WIDTH = 101
HEIGHT = 103

robots = []
with open("files/day14.txt", "r") as f:
    for line in f:
        split_l = line.split("\n")[0].split()
        p = list(map(int, split_l[0][2:].split(",")))
        v = list(map(int, split_l[1][2:].split(",")))
        robots.append([p, v])


# PART 01
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


# PART 02
bathroom = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for i in range(10000):
    if i % 10 == 0:
        print(i)
    new_bathroom = [l[:] for l in bathroom]
    for robot in robots:
        pos = robot[0]
        vel = robot[1]
        robot[0] = [(pos[0] + vel[0]) % WIDTH,
                    (pos[1] + vel[1]) % HEIGHT]
        new_bathroom[robot[0][1]][robot[0][0]] = 1
    fig, ax = plt.subplots()
    ax.imshow(new_bathroom, cmap="gray")
    fig.savefig("stupid_part_2\\{}.jpg".format(i))
    plt.close(fig)
