def rotate(direction):
    if direction == [0, -1]:
        return [1, 0]
    if direction == [1, 0]:
        return [0, 1]
    if direction == [0, 1]:
        return [-1, 0]
    if direction == [-1, 0]:
        return [0, -1]


maze = []
current_pos = [0, 0]
direction = [0, -1]
visited = []
with open("files/day06.txt", "r") as f:
    for i, line in enumerate(f):
        line_list = [" "] + list(line.split("\n")[0]) + [" "]
        maze.append(line_list)
        if "^" in line_list:
            current_pos[1] = i
            current_pos[0] = line_list.index("^")
            visited.append(current_pos)


# add padding
maze = [[" " for _ in range(len(maze[0]))]] + maze + [[" " for _ in range(len(maze[0]))]]


moving = True
while moving:
    new_pos = [sum(x) for x in zip(current_pos, direction)]
    if maze[new_pos[1]][new_pos[0]] == " ":
        moving = False
    elif maze[new_pos[1]][new_pos[0]] == "#":
        direction = rotate(direction)
    else:
        if new_pos not in visited:
            visited.append(new_pos)
        current_pos = new_pos


print(len(visited))
