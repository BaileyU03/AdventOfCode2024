with open("files/day11.txt", "r") as f:
    line = list(map(int, f.readline().split("\n")[0].split()))

for i in range(25):
    print(i)
    new_line = []
    for rock in line:
        s_rock = str(rock)
        if rock == 0:
            new_line.append(1)
        elif len(s_rock) % 2 == 0:
            new_line.append(int(s_rock[:len(s_rock)//2]))
            new_line.append(int(s_rock[len(s_rock)//2:]))
        else:
            new_line.append(rock*2024)
    line = new_line

print(len(line))
