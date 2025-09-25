lines = []
with open("./input") as f:
    lines = f.readlines()

total = 0
for curr in lines:
    split = [int(x) for x in curr.replace("\n", "").split("x")]
    assert len(split) == 3

    perimeters = [
        split[0] * 2 + split[1] * 2,
        split[1] * 2 + split[2] * 2,
        split[0] * 2 + split[2] * 2,
    ]

    required = min(perimeters) + split[0] * split[1] * split[2]
    total += required
print(total)
