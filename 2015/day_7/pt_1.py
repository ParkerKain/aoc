from typing import Any

lines = []
with open("./input") as f:
    lines = [x.replace("\n", "").split() for x in f.readlines()]


def lookup_definition(letter: str) -> list[str]:
    # print(f"Searching for {letter}")
    for curr_line in lines:
        if curr_line[-1] == letter:
            assert curr_line[-2] == "->"
            # print(f"Found!: {curr_line}")
            return curr_line[0:-2]

    raise ValueError(f"Cannot find {letter}")


def recursive_lookup(definition: list[str]) -> list[str]:
    new_definition: list[Any] = definition
    for i, curr in enumerate(definition):
        try:
            int(curr)
            new_definition[i] = [curr]
        except:
            if curr not in ["->", "x", "AND", "OR", "LSHIFT", "RSHIFT", "NOT"]:
                add_definition = lookup_definition(letter=curr)
                new_definition[i] = add_definition
            else:
                new_definition[i] = [curr]
    # print(new_definition)
    # flat_list = [x for xs in new_definition for x in xs]
    return new_definition


start = lookup_definition(letter="a")
test = recursive_lookup(definition=start)
test2 = recursive_lookup(definition=test)
test3 = recursive_lookup(definition=test2)
# print(test)
# print(test2)
print(test3)
