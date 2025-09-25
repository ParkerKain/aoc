line = ""
with open("./input") as f:
    line = f.readline()

final = 0
for i, curr in enumerate(line):
    if curr == "(":
        final += 1
    elif curr == ")":
        final -= 1

    if final == -1:
        print(i + 1)
        break
