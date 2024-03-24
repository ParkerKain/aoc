f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]

# lines = [
#     "...#......",
#     ".......#..",
#     "#.........",
#     "..........",
#     "......#...",
#     ".#........",
#     ".........#",
#     "..........",
#     ".......#..",
#     "#...#.....",
# ]

print("Iterating through rows ...")
galaxy_coords = []
rows_to_expand = []
for row_i, curr_row in enumerate(lines):
    galaxy_found_in_row = False
    for col_j, curr_char in enumerate(curr_row):
        if curr_char == "#":
            # print(f"Galaxy found at {row_i, col_j}")
            galaxy_coords.append((row_i, col_j))
            galaxy_found_in_row = True
    if not galaxy_found_in_row:
        rows_to_expand.append(row_i)

print("Iterating through cols ...")
num_cols = len(lines[0])
cols_to_expand = []
for col_j in range(num_cols):
    galaxy_found_in_col = False
    for row_i in range(len(lines)):
        if lines[row_i][col_j] == "#":
            galaxy_found_in_col = True
    if not galaxy_found_in_col:
        cols_to_expand.append(col_j)


print(f"Galaxy Coords: {galaxy_coords}")
print(f"Rows to expand: {rows_to_expand}")
print(f"Cols to expand: {cols_to_expand}")

# Time to expand
expanded_galaxies = []
for curr_gal in galaxy_coords:
    row_expands = sum([x < curr_gal[0] for x in rows_to_expand])
    col_expands = sum([x < curr_gal[1] for x in cols_to_expand])
    new_coords = (curr_gal[0] + row_expands * 999999, curr_gal[1] + col_expands * 999999)
    expanded_galaxies.append(new_coords)
    # print(f"Galaxy {curr_gal} is now {new_coords}")

# Now, get taxicab distance between all new coords
dists = []
for i, gal_1 in enumerate(expanded_galaxies):
    for j, gal_2 in enumerate(expanded_galaxies[i + 1 :]):
        # print(f"Comparing galaxy at {gal_1} to {gal_2}")
        taxicab_dist = abs(gal_2[0] - gal_1[0]) + abs(gal_2[1] - gal_1[1])
        # print(f"Distance is {taxicab_dist}")
        dists.append(taxicab_dist)

print(f"Total distance for {len(dists)} comparisons is {sum(dists)}")
