from itertools import permutations


# Helpful constants and dictionaries for getting pad information
NUMPAD = [[ 7,  8,  9 ],
          [ 4,  5,  6 ],
          [ 1,  2,  3 ],
          ["X", 0, "A"]]

ARROWPAD = [["X", "^", "A"],
            ["<", "v", ">"]]

numpad_dict = {}
for y, row in enumerate(NUMPAD):
    for x, num in enumerate(row):
        numpad_dict[num] = (x,y)
        numpad_dict[(x,y)] = num

arrowpad_dict = {}
for y, row in enumerate(ARROWPAD):
    for x, num in enumerate(row):
        arrowpad_dict[num] = (x,y)
        arrowpad_dict[(x,y)] = num


# Functions for getting the shortest arrow codes
def num_to_arrow(current_pos, code):
    new_pos = current_pos[:]
    arrow_string = ""
    key = code
    while new_pos[0] > numpad_dict[key][0]:
        new_pos = (new_pos[0] - 1, new_pos[1])
        arrow_string += "<"
    while new_pos[0] < numpad_dict[key][0]:
        new_pos = (new_pos[0] + 1, new_pos[1])
        arrow_string += ">"
    while new_pos[1] > numpad_dict[key][1]:
        new_pos = (new_pos[0], new_pos[1] - 1)
        arrow_string += "^"
    while new_pos[1] < numpad_dict[key][1]:
        new_pos = (new_pos[0], new_pos[1] + 1)
        arrow_string += "v"
    perms = [''.join(p) for p in permutations(arrow_string)]
    if key == "A":
        perms = [p for p in perms if p[-2:] != ">>"]
    elif key == 0:
        perms = [p for p in perms if p[-1:] != ">"]
    if numpad_dict[current_pos] == "A":
        perms = [p for p in perms if p[:2] != "<<"]
    elif numpad_dict[current_pos] == 0:
        perms = [p for p in perms if p[:1] != "<"]

    perms = [p + "A" for p in perms]
    perms = list(set(perms))
    return perms


def arrow_to_arrow(current_pos, code):
    if code == "":
        return [""]
    new_pos = current_pos[:]
    arrow_string = ""
    key = code[0]
    while new_pos[0] > arrowpad_dict[key][0]:
        new_pos = (new_pos[0] - 1, new_pos[1])
        arrow_string += "<"
    while new_pos[0] < arrowpad_dict[key][0]:
        new_pos = (new_pos[0] + 1, new_pos[1])
        arrow_string += ">"
    while new_pos[1] > arrowpad_dict[key][1]:
        new_pos = (new_pos[0], new_pos[1] - 1)
        arrow_string += "^"
    while new_pos[1] < arrowpad_dict[key][1]:
        new_pos = (new_pos[0], new_pos[1] + 1)
        arrow_string += "v"
    perms = [''.join(p) for p in permutations(arrow_string)]
    if arrow_string != "":
        if arrowpad_dict[current_pos] == "A":
            perms = [p for p in perms if p[:2] != "<<"]
        elif arrowpad_dict[current_pos] == "^":
            perms = [p for p in perms if p[:1] != "<"]
        if key == "A":
            perms = [p for p in perms if p[-2:] != ">>"]
        elif key == "^":
            perms = [p for p in perms if p[-1:] != ">"]
    else:
        perms = [""]
    perms = [p + "A" for p in perms]
    perms = list(set(perms))
    x = []
    for p in perms:
        thing = arrow_to_arrow(new_pos, code[1:])
        for r in thing:
            x.append(p + r)
    return x


# Parsing
codes = []
with open("files/day21.txt", "r") as f:
    for line in f:
        codes.append(line.split("\n")[0])

# Training
num_pairs = {}
for first in [0,1,2,3,4,5,6,7,8,9,"A"]:
    for second in [0,1,2,3,4,5,6,7,8,9,"A"]:
        num_pairs[str(first) + str(second)] = num_to_arrow(numpad_dict[first], second)

for num_pair in num_pairs.keys():
    second_layer = []
    for code in num_pairs[num_pair]:
        second_layer += arrow_to_arrow(arrowpad_dict["A"], code)
    third_layer = []
    for code in second_layer:
        third_layer += arrow_to_arrow(arrowpad_dict["A"], code)
    num_pairs[num_pair] = min(third_layer, key=len)


# Translating
total = 0
for code in codes:
    arrows = ""
    code_with_a = "A" + code
    for i in range(len(code)):
        arrows += num_pairs[str(code_with_a[i]) + str(code_with_a)[i + 1]]
    total += len(arrows) * int(code[:-1])
print(total)
