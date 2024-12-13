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
        xy = [int(new_line[0][2:]), int(new_line[1][2:])]
        if "A" in line:
            rule["A"] = xy
        elif "B" in line:
            rule["B"] = xy
        elif "P" in line:
            rule["P"] = xy
    rules.append(rule)


total1 = 0
total2 = 0
for rule in rules:
    a_mat = np.array([rule["A"], rule["B"]]).T
    # Part 1
    solution = np.linalg.solve(a_mat, np.array(rule["P"]))
    rounded = np.round(solution)
    if all(rounded == np.round(solution, 3)):       # Very rough way of checking for int
        total1 += solution @ np.array([3, 1])
    # Part 2
    new_p = np.array(list(map(lambda x: x + 10000000000000, rule["P"])))
    solution2 = np.linalg.solve(a_mat, new_p)
    rounded = np.round(solution2)
    if all(rounded == np.round(solution2, 3)):
        total2 += solution2 @ np.array([3, 1])

print(int(total1))
print(int(total2))
