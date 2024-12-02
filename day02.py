def part01():
    with open("./files/day02.txt", "r") as f:
        total = 0
        for line in f:
            split_line = list(map(int, line.split()))
            is_increasing = split_line[0] < split_line[-1]
            safe = line_checker(split_line, is_increasing)
            if safe:
                total += 1
        return total


def part02():
    with open("./files/day02.txt", "r") as f:
        total = 0
        for line in f:
            split_line = list(map(int, line.split()))
            safe = line_checker(split_line, True, True) or line_checker(split_line, False, True)
            if safe:
                total += 1
        return total


def line_checker(line, is_increasing, dampener=False):
    safe = True
    for i in range(len(line) - 1):
        if is_increasing and not (1 <= line[i + 1] - line[i] <= 3):
            if dampener:
                new_line1 = line[:]
                new_line1.pop(i)
                new_line2 = line[:]
                new_line2.pop(i + 1)
                return (line_checker(new_line1, True) or line_checker(new_line1, False)
                        or line_checker(new_line2, True) or line_checker(new_line2, False))
            safe = False
        if not is_increasing and not (1 <= line[i] - line[i + 1] <= 3):
            if dampener:
                new_line1 = line[:]
                new_line1.pop(i)
                new_line2 = line[:]
                new_line2.pop(i + 1)
                return (line_checker(new_line1, True) or line_checker(new_line1, False)
                        or line_checker(new_line2, True) or line_checker(new_line2, False))
            safe = False
    return safe


def main():
    print(part01())
    print(part02())


main()
