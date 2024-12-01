def part01(left, right):
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total


def part02(left, right):
    total = 0
    for loc in left:
        total += loc * right.count(loc)
    return total


def main():
    with open("./files/day01.txt", "r") as f:
        left = []
        right = []
        for line in f:
            split_line = line.split()
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))
        print(part01(left, right))
        print(part02(left, right))


main()
