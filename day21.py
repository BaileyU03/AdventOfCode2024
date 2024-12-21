from itertools import permutations


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


codes = []



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
    valid_perms = []
    if key == "A":
        for p in perms:
            if p[-2:] != ">>":
                valid_perms.append(p)
    elif key == 0:
        for p in perms:
            if p[-1:] != ">":
                valid_perms.append(p)
    else:
        valid_perms = perms
    if numpad_dict[current_pos] == "A":
        valid_perms = [p for p in valid_perms if p[:2] != "<<"]
    elif numpad_dict[current_pos] == 0:
        valid_perms = [p for p in valid_perms if p[:1] != "<"]


    valid_perms = [p + "A" for p in valid_perms]
    return valid_perms


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

    # perms = list(permutations(arrow_string))
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
    x = []
    for p in perms:
        thing = arrow_to_arrow(new_pos, code[1:])
        for r in thing:
            x.append(p + r)
    return x



with open("files/day21.txt", "r") as f:
    for line in f:
        codes.append(line.split("\n")[0])


# Training
s1 = {}
for first in [0,1,2,3,4,5,6,7,8,9,"A"]:
    for second in [0,1,2,3,4,5,6,7,8,9,"A"]:
        s1[str(first) + str(second)] = num_to_arrow(numpad_dict[first], second)

for num_pair in s1.keys():
    new = []
    for code in s1[num_pair]:
        new += arrow_to_arrow(arrowpad_dict["A"], code)
    nn = []
    for n in new:
        nn += arrow_to_arrow(arrowpad_dict["A"], n)
    s1[num_pair] = min(nn, key=len)


# Translating
total = 0
for code in codes:
    arrows = ""
    code_with_a = "A" + code
    for i in range(len(code)):
        arrows += s1[str(code_with_a[i]) + str(code_with_a)[i+1]]
    total += len(arrows) * int(code[:-1])
print(total)
