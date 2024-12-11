from functools import cache


@cache
def count(num, depth, limit):
    s_num = str(num)
    if depth == limit:
        return 1
    if num == 0:
        return count(1, depth + 1, limit)
    if len(s_num) % 2 == 0:
        return (count(int(s_num[:len(s_num) // 2]), depth + 1, limit)
              + count(int(s_num[len(s_num) // 2:]), depth + 1, limit))
    return count(num * 2024, depth + 1, limit)


with open("files/day11.txt", "r") as f:
    line = list(map(int, f.readline().split("\n")[0].split()))

total1 = 0
total2 = 0
for rock in line:
    total1 += count(rock, 0, 25)
    total2 += count(rock, 0, 75)
print(total1)
print(total2)
