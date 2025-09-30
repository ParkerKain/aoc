lines = []
with open("./input") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

good = 0

# lines = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
for curr_line in lines:
    pairs = {}
    skip = False
    good_pair = False
    # print(curr_line)
    for i, curr in enumerate(curr_line):
        if i == len(curr_line) - 1:
            continue

        # Evaluate pairs
        # if curr == curr_line[i + 1]:
        if curr_line[i : i + 2] not in pairs:
            pairs[curr_line[i : i + 2]] = [i]
        else:
            pairs[curr_line[i : i + 2]].append(i)

        if i == len(curr_line) - 2:
            continue
        # Evaluate skips
        if curr_line[i + 2] == curr:
            skip = True

    for k, v in pairs.items():
        if len(v) >= 3:
            good_pair = True
        elif len(v) == 2:
            if v[1] - v[0] > 1:
                good_pair = True

    # print(pairs, skip, good_pair)
    if skip and good_pair:
        good += 1
        # print("good")
print(good)
