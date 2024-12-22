def evolve(number):
    a = number * 64
    new_number = prune(mix(number, a))
    b = new_number // 32
    new_number = prune(mix(new_number, b))
    c = new_number * 2048
    new_number = prune(mix(new_number, c))
    return new_number


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216



starts = []
with open("files/day22.txt", "r") as f:
    for line in f:
        starts.append(int(line.split("\n")[0]))

ends = []
for start in starts:
    number = start
    for _ in range(2000):
        number = evolve(number)
    ends.append(number)

print(sum(ends))