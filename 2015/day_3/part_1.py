input = ""
with open("./input") as f:
    input = f.readline()
print(input)

visited = [(0, 0)]

coords = (0, 0)

for curr in input:
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

    if coords not in visited:
        visited.append(coords)
# print(visited)
print(len(visited))
