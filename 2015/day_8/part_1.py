lines = []
with open("./input") as f:
    lines = [x[0:-1] for x in f.readlines()]

total = 0
for curr_line in lines:
    # print(curr_line)
    len_long = len(curr_line)
    # print(repr(curr_line))
    # print(len(repr(curr_line)))
    # print(eval(curr_line))
    len_evaled = len(eval(curr_line))
    total = total + len_long - len_evaled

print(total)
