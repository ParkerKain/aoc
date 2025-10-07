line = ""
with open("./input") as f:
    line = f.readline().strip()

lines = line.split(", ")
print(lines)

lines = ["R2", "L3"]
lines = ["R2", "R2", "R2"]
lines = ["R5", "L5", "R5", "R3"]
lines = ["R5", "R5", "R5", "R5", "R5", "L5", "L5"]


coords = (0, 0)
facing_i = 0
facings = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for curr in lines:
    turn = curr[0]
    distance = int(curr[1])

    if turn == "R":
        facing_i = (facing_i + 1) % 4
    elif turn == "L":
        facing_i = (facing_i - 1) % 4
    else:
        raise ValueError
    assert facing_i in [0, 1, 2, 3]

    print(curr)
    print(facings[facing_i])
    new_x = coords[0] + facings[facing_i][0] * distance
    new_y = coords[1] + facings[facing_i][1] * distance
    coords = (new_x, new_y)
print(coords)
print(abs(coords[0]) + abs(coords[1]))
