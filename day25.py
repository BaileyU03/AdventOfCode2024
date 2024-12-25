keys = []
locks = []
with open("files/day25.txt", "r") as f:
    is_new_kl = True
    for line in f:
        if line == "\n":
            if is_key:
                keys.append(current[:])
            else:
                locks.append(current[:])
            is_new_kl = True
            continue
        clean_line = line.split("\n")[0]
        if is_new_kl:
            is_key = clean_line == "#####"
            current = [is_key * 1 for _ in range(5)]
            is_new_kl = False
        else:
            for i, char in enumerate(clean_line):
                if char == "#":
                    current[i] += 1
    if is_key:
        keys.append(current[:])
    else:
        locks.append(current[:])


total = 0
for k in keys:
    for l in locks:
        if all([sum(x) <= 7 for x in zip(k, l)]):
            total += 1
print(total)



