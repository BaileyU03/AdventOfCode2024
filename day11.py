from functools import cache


@cache
def x(num, depth, limit):
    s_num = str(num)
    if depth == limit:
        return 1
    if num == 0:
        return x(1, depth+1, limit)
    if len(s_num) % 2 == 0:
        return x(int(s_num[:len(s_num)//2]), depth+1, limit) + x(int(s_num[len(s_num)//2:]), depth+1, limit)
    return x(num*2024, depth+1, limit)


with open("files/day11.txt", "r") as f:
    line = list(map(int, f.readline().split("\n")[0].split()))

total1 = 0
total2 = 0
for rock in line:
    total1 += x(rock, 0, 25)
    total2 += x(rock, 0, 75)
print(total1)
print(total2)
