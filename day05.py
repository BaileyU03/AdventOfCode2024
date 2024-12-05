def main():
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

    valid_total = 0
    invalid_total = 0
    for update in updates:
        sorted_update = update[:]
        update_is_valid = True
        for i, page in enumerate(update):
            index_must_be_first = [j for j in range(len(rules[0])) if rules[0][j] == page]
            for index in index_must_be_first:
                if rules[1][index] in update[:i]:
                    update_is_valid = False
                    sorted_update = page_sort(update, rules)
            if not update_is_valid:
                break
            index_must_be_second = [j for j in range(len(rules[1])) if rules[1][j] == page]
            for index in index_must_be_second:
                if rules[0][index] in update[i + 1:]:
                    update_is_valid = False
                    sorted_update = page_sort(update, rules)
        if update_is_valid:
            valid_total += int(update[len(update)//2])
        else:
            invalid_total += int(sorted_update[len(sorted_update)//2])
    return valid_total, invalid_total


def page_sort(update, rules):
    # Bubble sort
    sorted = update[:]
    for i in range(len(sorted), 0, -1):
        for j in range(0, i - 1):
            if greater_than(sorted[j], sorted[j+1], rules):
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
    return sorted


def greater_than(a, b, rules):
    index_must_be_first = [j for j in range(len(rules[0])) if rules[0][j] == b]
    for index in index_must_be_first:
        if a == rules[1][index]:
            return True
    index_must_be_second = [j for j in range(len(rules[1])) if rules[0][j] == a]
    for index in index_must_be_second:
        if b == rules[0][index]:
            return True
    return False


print(main())
