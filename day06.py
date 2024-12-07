def simulate_guard(maze, current_pos, part2=False):
    # Gross (different return type depending on parameter lol) but it works
    direction = [0, -1]
    visited = []
    if part2:
        visited.append([current_pos] + [direction])
    else:
        visited.append(current_pos)
    moving = True
    while moving:
        new_pos = [sum(x) for x in zip(current_pos, direction)]
        if maze[new_pos[1]][new_pos[0]] == " ":
            moving = False
        elif maze[new_pos[1]][new_pos[0]] == "#":
            direction = rotate(direction)
        else:
            if part2:
                if [new_pos] + [direction] not in visited:
                    visited.append([new_pos] + [direction])
                    current_pos = new_pos
                else:
                    return True
            else:
                if new_pos not in visited:
                    visited.append(new_pos)
                current_pos = new_pos
    if part2:
        return False
    return visited


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
initial_pos = [0, 0]
with open("files/day06.txt", "r") as f:
    for i, line in enumerate(f):
        line_list = [" "] + list(line.split("\n")[0]) + [" "]
        maze.append(line_list)
        if "^" in line_list:
            initial_pos[1] = i
            initial_pos[0] = line_list.index("^")

# add padding
maze = [[" " for _ in range(len(maze[0]))]] + maze + [[" " for _ in range(len(maze[0]))]]

visited = simulate_guard(maze, initial_pos)

total = 0
for v in visited:
    new_maze = [x[:] for x in maze]
    new_maze[v[1]][v[0]] = "#"
    total += simulate_guard(new_maze, initial_pos, True)*1


print(len(visited))
print(total)
