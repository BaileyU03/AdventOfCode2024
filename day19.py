def is_possible(pattern, towels):
    if pattern == "":
        return True
    subpatterns = []
    for i in range(len(pattern)):
        if pattern[:i+1] in towels:
            subpatterns.append(pattern[i+1:])
    for subpattern in subpatterns:
        if is_possible(subpattern, towels):
            return True
    return False


patterns = []
with open("files/day19.txt", "r") as f:
    towels = f.readline().split("\n")[0].split(", ")
    f.readline()
    for line in f:
        patterns.append(line.split("\n")[0])


total = 0
for pattern in patterns:
    total += is_possible(pattern, towels)*1
print(total)
