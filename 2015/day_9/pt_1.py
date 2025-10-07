# Time to do a TSP!
from itertools import permutations

import pandas as pd

lines = []

with open("./input") as f:
    lines = [x.strip() for x in f.readlines()]

# lines = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]

map = {}
for curr in lines:
    start, _, end, _, dist = curr.split()
    dist = int(dist)

    if start not in map:
        map[start] = {}
    if end not in map:
        map[end] = {}
    map[start][end] = dist
    map[end][start] = dist

for curr in map.keys():
    map[curr][curr] = 0

dists = pd.DataFrame(map)
dists = dists.sort_index()
dists = dists.sort_index(axis=1)
print(dists)


all_orders = list(permutations(range(len(dists))))

answer = 999999999999999999999999999
for curr_order in all_orders:
    curr_dist = 0
    loc = curr_order[0]
    # print("=================")
    # print(curr_order)
    # print([dists.columns[x] for x in curr_order])
    for curr in curr_order[1:]:
        to_add = dists.loc[dists.columns[loc], dists.columns[curr]]
        curr_dist += to_add
        # print(f"{dists.columns[loc]} to {dists.columns[curr]}: {to_add}")
        loc = curr
    answer = min(answer, curr_dist)
    # print(f"{curr_dist}")
print(answer)
