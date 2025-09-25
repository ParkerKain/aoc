input = ""
with open("./input") as f:
    input = f.readline()
print(input)

visited = [(0, 0)]

all_coords = [(0, 0), (0, 0)]

for i, curr in enumerate(input):
    coords = all_coords[i % 2]
    if curr == "^":
        coords = (coords[0], coords[1] + 1)
    elif curr == ">":
        coords = (coords[0] + 1, coords[1])
    elif curr == "<":
        coords = (coords[0] - 1, coords[1])
    elif curr == "v":
        coords = (coords[0], coords[1] - 1)
    else:
        raise ValueError

    if i % 2 == 0:
        all_coords = [coords, all_coords[1]]
    else:
        all_coords = [all_coords[0], coords]

    if coords not in visited:
        visited.append(coords)
print(len(visited))
