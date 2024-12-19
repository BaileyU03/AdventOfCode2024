from functools import cache


@cache
def get_total_towel_arrangements(pattern, towels):
    if pattern == "":
        return 1
    subpatterns = []
    for i in range(len(pattern)):
        if pattern[:i+1] in towels:
            subpatterns.append(pattern[i+1:])
    return sum([get_total_towel_arrangements(s, towels) for s in subpatterns])


patterns = []
with open("files/day19.txt", "r") as f:
    towels = f.readline().split("\n")[0].split(", ")
    f.readline()
    for line in f:
        patterns.append(line.split("\n")[0])


total1 = 0
total2 = 0
for pattern in patterns:
    total1 += 1 if get_total_towel_arrangements(pattern, tuple(towels)) else 0
    total2 += get_total_towel_arrangements(pattern, tuple(towels))
print(total1)
print(total2)
