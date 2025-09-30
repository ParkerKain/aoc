lines = []

with open("./input") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

processed = []
for curr_line in lines:
    x = curr_line.split()

    if x[0] == "toggle":
        action = "toggle"
        start = [int(y) for y in x[1].split(",")]
        end = [int(y) for y in x[-1].split(",")]
    else:
        action = x[1]
        start = [int(y) for y in x[2].split(",")]
        end = [int(y) for y in x[-1].split(",")]

    final = [action, start, end]
    processed.append(final)

m = [[0] * 1000 for _ in range(1000)]


for curr_line in processed:
    action = curr_line[0]
    sx = curr_line[1][0]
    sy = curr_line[1][1]
    ex = curr_line[2][0]
    ey = curr_line[2][1]

    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            if action == "off":
                m[x][y] = max(0, m[x][y] - 1)
            elif action == "on":
                m[x][y] = m[x][y] + 1
            elif action == "toggle":
                m[x][y] = m[x][y] + 2
            else:
                raise ValueError

print(sum([sum(i) for i in m]))
