rules = [[], []]
updates = []
with open("files/day05.txt", "r") as f:
    mode = 0
    for line in f:
        if line == "\n":
            mode = 1
            continue
        if mode == 0:
            l = line.split("\n")[0].split("|")
            rules[0].append(l[0])
            rules[1].append(l[1])
        else:
            updates.append(line.split("\n")[0].split(","))


total = 0
for update in updates:
    update_is_valid = True
    for i, page in enumerate(update):
        index_must_be_first = [j for j in range(len(rules[0])) if rules[0][j] == page]
        for index in index_must_be_first:
            if rules[1][index] in update[:i]:
                update_is_valid = False
                break
        if not update_is_valid:
            break
        index_must_be_second = [j for j in range(len(rules[1])) if rules[1][j] == page]
        for index in index_must_be_first:
            if rules[0][index] in update[i + 1:]:
                update_is_valid = False
                break
    if update_is_valid:
        total += int(update[len(update)//2])


print(total)
