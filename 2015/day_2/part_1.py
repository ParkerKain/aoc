lines = []
with open("./input") as f:
    lines = f.readlines()

total = 0
for curr in lines:
    split = [int(x) for x in curr.replace("\n", "").split("x")]
    assert len(split) == 3

    # print(split)
    areas = [split[0] * split[1], split[1] * split[2], split[0] * split[2]]
    # print(areas)

    required = sum(areas) * 2 + min(areas)
    # print(required)
    total += required
print(total)
