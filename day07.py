def is_valid_rule(rule):
    if len(rule) == 2:
        if rule[0] == rule[1]:
            return True
        else:
            return False
    rule_after_add = [rule[0] - rule[-1]] + rule[1:-1]
    if rule[0] % rule[-1] == 0:
        rule_after_mul = [rule[0] // rule[-1]] + rule[1:-1]
        return is_valid_rule(rule_after_mul) or is_valid_rule(rule_after_add)
    return is_valid_rule(rule_after_add)


rules = []
with open("files/day07.txt", "r") as f:
    for line in f:
        rules.append(list(map(int, line.replace(":", "").split())))


total = 0
for rule in rules:
    if is_valid_rule(rule[:]):
        total += rule[0]


print(total)
