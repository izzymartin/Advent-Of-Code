# Day 5: Hydrothermal Venture

# function for part 1
#   Counts the number of overlapping lines
def vent_overlap(input, map_x_size, map_y_size):
    map = []
    for x in range(map_y_size):
        map.append([int(0) for y in range(map_x_size)])

    input_split = input.split("\n")
    for line in input_split:
        entry = line.split(" -> ")
        start = entry[0].split(",")
        end = entry[1].split(",")

        x_diff = int(end[0]) - int(start[0])
        y_diff = int(end[1]) - int(start[1])

        if x_diff != 0 and y_diff == 0:
            x_pos = int(start[0])
            y_pos = int(start[1])
            map[x_pos][y_pos] += 1
            while x_pos != int(end[0]):
                if x_diff < 0:
                    x_pos -= 1
                else:
                    x_pos += 1
                map[x_pos][y_pos] += 1
        elif x_diff == 0 and y_diff != 0:
            x_pos = int(start[0])
            y_pos = int(start[1])
            map[x_pos][y_pos] += 1
            while y_pos != int(end[1]):
                if y_diff < 0:
                    y_pos -= 1
                else:
                    y_pos += 1
                map[x_pos][y_pos] += 1
    intersect_count = 0
    for map_x in range(map_x_size):
        for map_y in range(map_y_size):
            intersect_count += (map[map_x][map_y] > 1)
    return intersect_count


# function for part 2
#   Counts the number of overlapping lines, including diagonal lines
def vent_overlap_diagonal(input, map_x_size, map_y_size):
    map = []
    for x in range(map_y_size):
        map.append([int(0) for y in range(map_x_size)])

    input_split = input.split("\n")
    for line in input_split:
        entry = line.split(" -> ")
        start = entry[0].split(",")
        end = entry[1].split(",")

        x_diff = int(end[0]) - int(start[0])
        y_diff = int(end[1]) - int(start[1])

        if x_diff != 0 and y_diff == 0:
            x_pos = int(start[0])
            y_pos = int(start[1])
            map[x_pos][y_pos] += 1
            while x_pos != int(end[0]):
                if x_diff < 0:
                    x_pos -= 1
                else:
                    x_pos += 1
                map[x_pos][y_pos] += 1
        elif x_diff == 0 and y_diff != 0:
            x_pos = int(start[0])
            y_pos = int(start[1])
            map[x_pos][y_pos] += 1
            while y_pos != int(end[1]):
                if y_diff < 0:
                    y_pos -= 1
                else:
                    y_pos += 1
                map[x_pos][y_pos] += 1
        elif abs(x_diff) == abs(y_diff):
            x_pos = int(start[0])
            y_pos = int(start[1])
            map[x_pos][y_pos] += 1
            while y_pos != int(end[1]):
                if y_diff < 0:
                    y_pos -= 1
                else:
                    y_pos += 1
                if x_diff < 0:
                    x_pos -= 1
                else:
                    x_pos += 1
                map[x_pos][y_pos] += 1
    intersect_count = 0
    for map_x in range(map_x_size):
        for map_y in range(map_y_size):
            intersect_count += (map[map_x][map_y] > 1)
    return intersect_count


with open("inputs/day5test.txt", "r+") as file:
    test_input = file.read()
file.close()

with open("inputs/day5data.txt", "r+") as file:
    data_input = file.read()
file.close()

# call each function with test and data for part 1 and part 2
test_vent_overlap = vent_overlap(test_input,10,10)
print(f"Part 1 test vent overlap: {test_vent_overlap}")

data_vent_overlap = vent_overlap(data_input,1000,1000)
print(f"Part 1 data vent overlap: {data_vent_overlap}")

test_vent_overlap_diagonal = vent_overlap_diagonal(test_input,10,10)
print(f"Part 2 test vent overlap: {test_vent_overlap_diagonal}")

data_vent_overlap_diagonal = vent_overlap_diagonal(data_input,1000,1000)
print(f"Part 2 data vent overlap: {data_vent_overlap_diagonal}")
