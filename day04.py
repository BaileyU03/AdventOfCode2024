def is_west(w, x, y):
    if x < 3:
        return False
    if w[y][x-1] == "M" and w[y][x-2] == "A" and w[y][x-3] == "S":
        return True
    return False


def is_east(w, x, y):
    if x > len(w) - 4:
        return False
    if w[y][x+1] == "M" and w[y][x+2] == "A" and w[y][x+3] == "S":
        return True
    return False


def is_north(w, x, y):
    if y < 3:
        return False
    if w[y-1][x] == "M" and w[y-2][x] == "A" and w[y-3][x] == "S":
        return True
    return False


def is_south(w, x, y):
    if y > len(w[x]) - 4:
        return False
    if w[y+1][x] == "M" and w[y+2][x] == "A" and w[y+3][x] == "S":
        return True
    return False


def is_northwest(w, x, y):
    if y < 3 or x < 3:
        return False
    if w[y-1][x-1] == "M" and w[y-2][x-2] == "A" and w[y-3][x-3] == "S":
        return True
    return False


def is_northeast(w, x, y):
    if y < 3 or x > len(w) - 4:
        return False
    if w[y-1][x+1] == "M" and w[y-2][x+2] == "A" and w[y-3][x+3] == "S":
        return True
    return False


def is_southwest(w, x, y):
    if y > len(w[x]) - 4 or x < 3:
        return False
    if w[y+1][x-1] == "M" and w[y+2][x-2] == "A" and w[y+3][x-3] == "S":
        return True
    return False


def is_southeast(w, x, y):
    if y > len(w[x]) - 4 or x > len(w) - 4:
        return False
    if w[y+1][x+1] == "M" and w[y+2][x+2] == "A" and w[y+3][x+3] == "S":
        return True
    return False


def get_xmass(w, x, y):
    return (is_north(w, x, y)*1 + is_south(w, x, y)*1 + is_west(w, x, y)*1 + is_east(w, x, y)*1
            + is_northwest(w, x, y)*1 + is_northeast(w, x, y)*1 + is_southwest(w, x, y)*1 + is_southeast(w, x, y)*1)


wordsearch = []
with open("./files/day04.txt", "r") as f:
    for line in f:
        wordsearch.append(list(line.split("\n")[0]))

total = 0
for y, row in enumerate(wordsearch):
    for x, char in enumerate(row):
        if char == "X":
            total += get_xmass(wordsearch,x,y)

print(total)

