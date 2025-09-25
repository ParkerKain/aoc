line = ""
with open("./input") as f:
    line = f.readline()

final = 0
for curr in line:
    if curr == "(":
        final += 1
    elif curr == ")":
        final -= 1
print(final)
