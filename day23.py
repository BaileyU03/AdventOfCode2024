adj_list = {}
with open("files/day23.txt", "r") as f:
    for line in f:
        split_line = line.split("\n")[0].split("-")
        if split_line[0] in adj_list.keys():
            adj_list[split_line[0]].append(split_line[1])
        else:
            adj_list[split_line[0]] = [split_line[1]]
        if split_line[1] in adj_list.keys():
            adj_list[split_line[1]].append(split_line[0])
        else:
            adj_list[split_line[1]] = [split_line[0]]


# Part 01
tris = []
ts = [n for n in adj_list if n[0] == "t"]
visited_ts = []     # for ignoring duplicates
for t in ts:
    visited_ts.append(t)
    adj_to_t = adj_list[t]
    for i in range(len(adj_to_t) - 1):
        a = adj_to_t[i]
        if a in visited_ts:
            continue
        for j in range(i + 1, len(adj_to_t)):
            b = adj_to_t[j]
            if b in visited_ts:
                continue
            if b in adj_list[a]:
                tris.append((t, a, b))


# Part 02
biggest_cliques = [[k] for k in adj_list.keys()]
next_clique_size = [[]]
while len(next_clique_size) > 0:
    next_clique_size = []
    for clique in biggest_cliques:
        for new_v in adj_list.keys():
            if new_v in clique:
                continue
            adj_to_all = True
            for v in clique:
                if new_v not in adj_list[v]:
                    adj_to_all = False
                    break
            if adj_to_all:
                new_clique = clique + [new_v]
                new_clique.sort()
                if new_clique not in next_clique_size:
                    next_clique_size.append(new_clique)
    if len(next_clique_size) > 0:
        biggest_cliques = next_clique_size[:]

print(",".join(biggest_cliques[0]))
