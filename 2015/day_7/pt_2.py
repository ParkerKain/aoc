lines = []
with open("./input") as f:
    lines = [x.replace("\n", "").split() for x in f.readlines()]

definitions = {}

# Make all the blank definitions
for curr_line in lines:
    for element in curr_line:
        if (
            element not in ["OR", "AND", "LSHIFT", "RSHIFT", "NOT", "->"]
            and element not in definitions
        ):
            try:
                int(element)
            except:
                definitions[element] = None


def get_val(i: str):
    try:
        return int(i)
    except:
        return definitions[i]


def print_non_nulls():
    print("==========================")
    for k, v in definitions.items():
        if v is not None:
            print(k, v)


def process():
    for curr_line in lines:
        factors = [x for x in curr_line[:-2] if x in definitions]
        if all([definitions[x] is not None for x in factors]):
            assign_to = curr_line[-1]
            if definitions[assign_to] is not None:
                continue
            if len(curr_line) == 3:
                to_assign = get_val(curr_line[0])
                definitions[assign_to] = to_assign
            elif len(curr_line) == 4:
                start = get_val(curr_line[1])
                to_assign = ~start
                definitions[assign_to] = to_assign
            elif len(curr_line) == 5:
                operand = curr_line[1]
                start = get_val(curr_line[0])
                end = get_val(curr_line[2])
                if operand == "LSHIFT":
                    to_assign = start << end
                elif operand == "RSHIFT":
                    to_assign = start >> end
                elif operand == "AND":
                    to_assign = start & end
                elif operand == "OR":
                    to_assign = start | end
                else:
                    raise ValueError(f"Unknown operand {operand}")
                definitions[assign_to] = to_assign
            else:
                raise ValueError(f"unsure what to do with {curr_line}")


while definitions["a"] is None:
    process()
    # print_non_nulls()
to_apply = definitions["a"]
print(to_apply)
for k in definitions.keys():
    definitions[k] = None
definitions["b"] = to_apply
assert definitions["a"] is None
print(definitions)
while definitions["a"] is None:
    process()
print("Final Answer! " + str(definitions["a"]))
