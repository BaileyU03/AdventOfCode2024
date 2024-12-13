import numpy as np


rules = []
with open("files/day13.txt", "r") as f:
    rule = {}
    for line in f:
        if line == "\n":
            rules.append(rule)
            rule = {}
            continue
        new_line = line.split("\n")[0].split(": ")[1].split(", ")
        xy = np.array([int(new_line[0][2:]), int(new_line[1][2:])])
        if "A" in line:
            rule["A"] = xy
        elif "B" in line:
            rule["B"] = xy
        elif "P" in line:
            rule["P"] = xy
    rules.append(rule)


total = 0
for rule in rules:
    min_tokens = -1
    A = rule["A"]
    B = rule["B"]
    P = rule["P"]
    a = min(rule["P"] // rule["A"])
    b = 0
    while a >= 0:
        while all(a*A + b*B < P):
            b += 1
        if all(a*A + b*B == P):
            if min_tokens == -1:
                min_tokens = 3*a + b
            else:
                min_tokens = min(min_tokens, 3*a + b)
        a -= 1
    total += min_tokens if min_tokens > -1 else 0

print(total)
