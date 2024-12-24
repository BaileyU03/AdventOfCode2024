def operate(a, b, operand):
    if operand == "AND":
        return a & b
    if operand == "OR":
        return a | b
    if operand == "XOR":
        return a ^ b


values = {}
instructions = []
with open("files/day24.txt", "r") as f:
    values_mode = True
    for line in f:
        if line == "\n":
            values_mode = False
            continue
        if values_mode:
            split_line = line.split("\n")[0].split(": ")
            values[split_line[0]] = int(split_line[1])
        else:
            split_line = line.split("\n")[0].split(" ")
            instructions.append({"op1": split_line[0],
                                 "op2": split_line[2],
                                 "ins": split_line[1],
                                 "res": split_line[4]})


zs = sorted([a["res"] for a in instructions if a["res"][0] == "z"])
while len(zs) > len([a for a in values.keys() if a[0] == "z"]):
    new_instructions = []
    for instruction in instructions:
        if instruction["op1"] in values.keys() and instruction["op2"] in values.keys():
            values[instruction["res"]] = operate(values[instruction["op1"]],
                                                 values[instruction["op2"]],
                                                 instruction["ins"])
        else:
            new_instructions.append(instruction)
    instructions = new_instructions


result = 0
exp = 0
for z in zs:
    result += values[z] * 2**exp
    exp += 1
print(result)

