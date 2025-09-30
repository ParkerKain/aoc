lines = []
with open("./input") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

good = 0
for curr_line in lines:
    vowel_count = 0
    double_letter = False
    bad = False
    for i, curr in enumerate(curr_line):
        # print(i, curr)
        if curr in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
            # print("Vowel!")
        if i != len(curr_line) - 1:
            if curr == curr_line[i + 1]:
                double_letter = True
                # print("Double Letter!")
        if curr_line[i : i + 2] in ["ab", "cd", "pq", "xy"]:
            # print("Oh No!")
            bad = True
    if vowel_count >= 3 and double_letter and not bad:
        good += 1
        # print("Good!")
print(good)
