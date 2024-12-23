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

print(len(tris))
