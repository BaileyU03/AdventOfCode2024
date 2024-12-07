def is_valid_rule(rule):
    if len(rule) == 2:
        return rule[0] == rule[1]
    rule_after_add = [rule[0] - rule[-1]] + rule[1:-1]
    if rule[0] % rule[-1] == 0:
        rule_after_mul = [rule[0] // rule[-1]] + rule[1:-1]
        return is_valid_rule(rule_after_mul) or is_valid_rule(rule_after_add)
    return is_valid_rule(rule_after_add)


def is_valid_rule_part2(rule):
    # more naive :( but only runs if there's no solution w/o concatenation
    if len(rule) == 2:
        return rule[0] == rule[1]
    rule_after_add = [rule[0]] + [rule[1] + rule[2]] + rule[3:]
    rule_after_mul = [rule[0]] + [rule[1] * rule[2]] + rule[3:]
    rule_after_con = [rule[0]] + [concatenate(rule[1], rule[2])] + rule[3:]
    return is_valid_rule_part2(rule_after_add) or is_valid_rule_part2(rule_after_mul) or is_valid_rule_part2(rule_after_con)


def concatenate(a, b):
    return int(str(a) + str(b))


rules = []
with open("files/day07.txt", "r") as f:
    for line in f:
        rules.append(list(map(int, line.replace(":", "").split())))

total1 = 0
total2 = 0
for rule in rules:
    if is_valid_rule(rule[:]):
        total1 += rule[0]
    elif is_valid_rule_part2(rule[:]):
        total2 += rule[0]

total2 += total1

print(total1, total2)
