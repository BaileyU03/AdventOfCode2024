import re

with open("./files/day03.txt", "r") as f:
    muls = []
    for line in f:
        while "mul" in line:
            mul_pos = line.find("mul")
            try:
                muls.append(line[mul_pos+3:mul_pos+13])
                line = line[0:mul_pos] + line[mul_pos+3:]
            except IndexError:
                muls.append(line[mul_pos:])
                line = line[0:mul_pos]

    total = 0
    for m in muls:
        match = re.search("^\(\d{1,3},\d{1,3}\)", m)
        if match is not None:
            pair = list(map(int, match.group()[1:-1].split(",")))
            total += pair[0] * pair[1]
    print(total)
