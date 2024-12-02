with open("./files/day02.txt", "r") as f:
    total = 0
    for line in f:
        split_line = list(map(int, line.split()))
        safe = True
        is_increasing = split_line[0] < split_line[-1]
        for i in range(len(split_line) - 1):
            if is_increasing and not (1 <= split_line[i+1] - split_line[i] <= 3):
                safe = False
                break
            if not is_increasing and not (1 <= split_line[i] - split_line[i+1] <= 3):
                safe = False
                break
        if safe:
            total += 1
    print(total)
